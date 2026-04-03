# 🏎 Pitlane Project | F1 Stats Manager

Sistema de gerenciamento e telemetria de Fórmula 1 desenvolvido com **Django, MySQL e Docker**.

Projeto completo que permite gerenciar pilotos, equipes e estatísticas históricas da F1, consumindo dados reais de APIs de automobilismo. Possui interface administrativa e pública personalizada com o tema **Carbon & Red**.

---

## 📋 Índice

* [🛠 Tecnologias](#-tecnologias)
* [✨ Funcionalidades](#-funcionalidades)
* [📁 Estrutura do Projeto](#-estrutura-do-projeto)
* [🚀 Começando](#-começando-docker)
* [🏎 Sincronização de Dados](#-sincronização-de-dados)
* [📊 Entidades](#-entidades)
* [🎨 Interface Visual](#-interface-visual)
* [🔧 Troubleshooting](#-troubleshooting)
* [📝 Autor](#-autor)

---

## 🛠 Tecnologias

* Python 3.13
* Django 5.1
* MySQL 8.0 (porta 3307)
* Docker & Docker Compose
* Django REST Framework
* Bootstrap 5
* Ergast API / OpenF1

---

## ✨ Funcionalidades

* ✅ **Dashboard de Temporadas**: filtro dinâmico (2020–2024)
* ✅ **Gestão de Equipes**: vínculo automático de pilotos
* ✅ **Perfil de Piloto**: telemetria e histórico de performance
* ✅ **Autenticação Paddock**: login e cadastro de usuários
* ✅ **Sincronizador Customizado**: importação via CLI
* ✅ **Interface Carbon & Red**: UI inspirada na F1
* ✅ **API REST**: endpoints para integração externa

---

## 📁 Estrutura do Projeto

```
pitlane-project/
├── config/
│   ├── settings.py
│   └── urls.py
├── pilotos/
│   ├── models.py
│   ├── views.py
│   ├── management/
│   └── serializers.py
├── times/
│   ├── models.py
│   ├── views.py
│   └── serializers.py
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── cadastro.html
│   ├── pilotos/
│   └── times/
├── static/
│   └── css/style.css
├── docker-compose.yml
├── Dockerfile
└── manage.py
```

---

## 🚀 Começando (Docker)

### Pré-requisitos

* Docker Desktop instalado

### Passos

#### 1. Clone o repositório

```bash
git clone https://github.com/josehmelo/pitlane-f1.git
cd pitlane-f1
```

#### 2. Suba os containers

```bash
docker-compose up --build -d
```

#### 3. Prepare o ambiente

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

#### 4. Acesse o sistema

```
http://localhost:8000/login/
```

---

## 🏎 Sincronização de Dados

Importe dados reais da F1 diretamente para o banco:

### Temporada atual

```bash
docker-compose exec web python manage.py sync_season 2024
```

### Temporadas anteriores

```bash
docker-compose exec web python manage.py sync_season 2023
```

---

## 📊 Entidades

### 🧑‍✈️ Modelo: Piloto

| Campo     | Tipo       | Descrição               |
| --------- | ---------- | ----------------------- |
| nome      | CharField  | Primeiro nome do piloto |
| sobrenome | CharField  | Sobrenome oficial       |
| numero    | Integer    | Número no grid          |
| equipe    | ForeignKey | Relação com Time        |

---

### 📈 Modelo: Piloto_Status

| Campo     | Tipo      | Descrição                    |
| --------- | --------- | ---------------------------- |
| temporada | CharField | Ano da competição (ex: 2024) |
| pontos    | Decimal   | Total de pontos              |
| posicao   | Integer   | Ranking atual/final          |
| vitorias  | Integer   | Número de vitórias           |

---

## 🎨 Interface Visual

Tema customizado inspirado na identidade da Fórmula 1:

* **Background:** `#15151e` (Dark Mode)
* **Primary:** `#e10600` (F1 Racing Red)
* **Cards:** `#1f1f27` (Carbon Style)

---

## 🔧 Troubleshooting

### ❌ Porta 3306 ocupada

O projeto usa a porta **3307** para evitar conflitos.
Verifique o `docker-compose.yml`.

---

### ❌ CSS não atualiza

* Use `Ctrl + F5`
* Limpe o cache do navegador

---

## 📝 Autor

**José Melo**
🎓 Computer Science Student


---

📅 Última atualização: Abril 2026
