# Pitlane-Projec

Pitlane Project | F1 Stats ManagerSistema de gerenciamento e telemetria de Fórmula 1 com Django, MySQL e DockerUm projeto robusto que permite gerenciar pilotos, equipes e estatísticas históricas da F1. O sistema consome dados reais de APIs de automobilismo, permite a filtragem dinâmica por temporadas (2020-2024) e possui uma interface administrativa e pública personalizada com o tema Carbon & Red.📋 ÍndiceTecnologiasFuncionalidadesEstrutura do ProjetoComeçandoSincronização de DadosInterface VisualEntidadesTroubleshooting🛠 TecnologiasPython 3.13Django 5.1MySQL 8.0 (Porta customizada 3307)Docker & Docker ComposeDjango REST Framework (API REST)Bootstrap 5 (Interface Web)Ergast API / OpenF1 (Fontes de dados)✨ Funcionalidades✅ Dashboard de Temporadas: Filtro dinâmico para visualizar o grid de diferentes anos.✅ Gestão de Equipes: Detalhamento de escuderias com vinculação automática de pilotos.✅ Perfil de Piloto: Telemetria individual e histórico de performance.✅ Autenticação Paddock: Sistema de login e cadastro para acesso à área restrita.✅ Sincronizador Customizado: Comando CLI para importar dados de temporadas específicas.✅ Interface Carbon & Red: UI customizada inspirada na identidade visual da F1.✅ API REST: Endpoints documentados para integração mobile.📁 Estrutura do Projetopitlane-project/
├── config/                 # Configurações centrais do Django
│   ├── settings.py         # Configurações de DB e Apps
│   └── urls.py             # Rotas globais (Admin, API, Web)
├── pilotos/                # App de Atletas e Performance
│   ├── models.py           # Modelos Piloto e Piloto_Status
│   ├── views.py            # Lógica de ranking e temporadas
│   ├── management/         # Comandos customizados (sync_season)
│   └── serializers.py      # Transformação de dados para API
├── times/                  # App de Construtores
│   ├── models.py           # Modelo de Equipes (Escuderias)
│   ├── views.py            # Lógica de line-up por equipe
│   └── serializers.py      # Serializers de times
├── templates/              # Interface Web (HTML/Django)
│   ├── base.html           # Layout principal com Navbar F1
│   ├── login.html          # Tela de acesso ao Paddock
│   ├── cadastro.html       # Registro de novos usuários
│   ├── pilotos/            # Listagem e Detalhes de Pilotos
│   └── times/              # Grid e Detalhes de Equipes
├── static/                 # Arquivos Estáticos
│   └── css/style.css       # Tema Custom Carbon & Red
├── docker-compose.yml      # Orquestração (Web + MySQL 3307)
├── Dockerfile              # Definição da imagem Python
└── manage.py
🚀 Começando (Docker)Pré-requisitosDocker Desktop instaladoPassos:Clone e entre na pastaBashgit clone https://github.com/josehmelo/pitlane-f1.git
cd pitlane-f1
Suba os containersBashdocker-compose up --build -d
Prepare o ambienteBashdocker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
Acessehttp://localhost:8000/login/
🏎 Sincronização de DadosO projeto possui um comando exclusivo para alimentar o banco de dados MySQL com dados reais da F1.Para importar a temporada atual:Bashdocker-compose exec web python manage.py sync_season 2024
Para importar dados históricos:Bashdocker-compose exec web python manage.py sync_season 2023
📊 EntidadesModelo: PilotoCampoTipoDescriçãonomeCharFieldPrimeiro nome do pilotosobrenomeCharFieldSobrenome oficialnumeroIntegerNúmero permanente no gridequipeForeignKeyVínculo com o modelo TimeModelo: Piloto_Status (Estatísticas)CampoTipoDescriçãotemporadaCharFieldAno da competição (ex: 2024)pontosDecimalTotal de pontos acumuladosposicaoIntegerPosição final/atual no rankingvitoriasIntegerQuantidade de GPs vencidos🎨 Interface VisualO projeto utiliza uma folha de estilo customizada (style.css) que sobrescreve o Bootstrap para criar a estética Carbon Dark:Background: #15151e (Dark Mode F1)Primary: #e10600 (F1 Racing Red)Cards: #1f1f27 (Carbon Fiber Texture)🔧 TroubleshootingErro: Porta 3306 ocupadaO projeto está configurado para usar a porta 3307 no host para evitar conflitos com MySQLs locais. Verifique o docker-compose.yml.CSS não carrega as cores novasDevido ao cache agressivo do navegador, use Ctrl + F5 ou limpe o cache do navegador após alterar o style.css.Bandeiras não aparecem ou estão erradasAs bandeiras foram removidas para garantir um design mais limpo e independente de APIs externas. O foco atual é na tipografia e dados técnicos.📝 AutorJose Melo - Computer Science StudentMarketing & Video Production Background aplicado ao desenvolvimento de software.Última atualização: Abril 2026
