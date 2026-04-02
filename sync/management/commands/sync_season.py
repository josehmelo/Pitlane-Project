from django.core.management.base import BaseCommand
from times.models import Time
from pilotos.models import Piloto, Piloto_Status
from sync.services import jolpica, openf1

class Command(BaseCommand):
    help = 'Sincroniza os dados da temporada atual'
    
    def add_arguments(self, parser):
        parser.add_argument('ano', type=int, help='Ano da temporada a ser sincronizada')
        
    def handle(self, *args, **kwargs):
        ano = kwargs['ano']
        self.stdout.write(f'Sincronizando dados da temporada {ano}...')
        
        self.sync_times(ano)
        self.sync_pilotos(ano)
        self.sync_stats(ano)
        
        self.stdout.write(self.style.SUCCESS(f'\nSync da temporada {ano} concluído!\n'))
        
    def sync_times(self, ano):
        self.stdout.write('Sincronizando times...')
        construtores = jolpica.get_construtores(ano)
        qualificacao_dict = {s['Constructor']['constructorId']: s for s in jolpica.construtor_qualificacao(ano)}
        
        for c in construtores:
            construtor_id = c['constructorId']
            qual_data = qualificacao_dict.get(construtor_id, {})
            vitorias = int(qual_data.get('wins', 0))
            
            time, criado = Time.objects.update_or_create(
                construtor_id=construtor_id,
                defaults={
                    'nome': c['name'],
                    'nome_completo': c['name'],
                    'nacionalidade': c.get('nationality', ''),
                    'base': '',
                    'campeonatos': vitorias,
                    'atividade': True,
                }
            )
            
            status = 'Criado' if criado else 'Atualizado'
            self.stdout.write(f'  Equipe {status}: {time.nome}')
    def sync_pilotos(self, ano):
        self.stdout.write('Sincronizando pilotos...')
        pilotos = jolpica.get_pilotos(ano)
        
        openf1_pilotos={}
        try:
            for p in openf1.get_pilotos(ano):
                if p.get('piloto_numero'):
                    openf1_pilotos[p.get('nome__acronym', '')] = p
        except Exception:
            self.stdout.write(self.style.WARNING('  Falha ao obter dados de pilotos do OpenF1. Continuando com os dados do Jolpica...'))
        
        for p in pilotos:
                piloto_id = p['driverId']
                codigo = p.get('code', '')
                openf1_data = openf1_pilotos.get(codigo, {})
                numero = openf1_data.get('piloto_numero') or  p.get('permanentNumber')
                try:
                    numero = int(numero) if numero else None
                except(ValueError, TypeError):
                    numero = None
                    
                try:
                    from datetime import date
                    dob = date.fromisoformat(p.get('dateOfBirth')) if p.get('dateOfBirth') else None
                except ValueError:
                    dob = None
                    
                piloto, criado = Piloto.objects.update_or_create(
                    piloto_id=piloto_id,
                    defaults={
                        'nome': p['givenName'],
                        'sobrenome': p['familyName'],
                        'nacionalidade': p.get('nationality', ''),
                        'codigo': codigo,
                        'aniversario': dob,
                        'numero': numero,
                        'atividade': True,
                    }
                )
                status = 'criado' if criado else 'atualizado'
                self.stdout.write(f'  Piloto {status}: {piloto}')
                
    def sync_stats(self, ano):
        self.stdout.write('Buscando estatísticas...')
        qualificacao = jolpica.get_pilotos_qualificacao(ano)

        for s in qualificacao:
            piloto_id = s['Driver']['driverId']
            try:
                piloto = Piloto.objects.get(piloto_id=piloto_id)
            except Piloto.DoesNotExist:
                continue

            # vincula o piloto à equipe
            if s.get('Constructors'):
                construtor_id = s['Constructors'][0]['constructorId']
                try:
                    time = Time.objects.get(construtor_id=construtor_id)
                    piloto.equipe = time
                    piloto.save()
                except Time.DoesNotExist:
                    pass

            Piloto_Status.objects.update_or_create(
                piloto=piloto,
                temporada=ano,
                defaults={
                    'vitorias': int(s.get('wins', 0)),
                    'pontos': int(s.get('points', 0)),
                    'posicao': int(s.get('position', 0)),
                    'podiums': 0,
                    'poles': 0,
                }
            )
            self.stdout.write(f'  Stats atualizadas: {piloto} ({ano})')
