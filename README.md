# 🐍 Python Clean Architecture + TDD

## 📌 Descrição do Treinamento

Este treinamento tem como objetivo ensinar a criação de uma API em Python seguindo os princípios da Clean Architecture e aplicando Test-Driven Development (TDD).
Você aprenderá a estruturar um projeto profissional, garantindo baixo acoplamento, alta testabilidade e facilidade de manutenção.

Ao final, você terá construído uma API simples, rodando com PostgreSQL e coberta por testes automatizados.

### ⚙️ Requisitos Técnicos

- **Python 3.12** ou superior
- **Poetry** Para gerenciamento de pacotes
- **Docker** para execução do PostgreSQL localmente
- Uma ferramenta de conexão com banco de dados (escolha uma):
  - [Beekeeper Studio](https://www.beekeeperstudio.io/) - Interface moderna e intuitiva para gerenciamento de bancos de dados
  - [Sqlectron](https://sqlectron.github.io/) - Cliente SQL leve e multiplataforma
  - Ou qualquer outra ferramenta de sua preferência (DBeaver, pgAdmin, etc.)

### Estrutura do Projeto

Ao jogar no readme essa estrutura aqui, não fica formatado corretamente. 

Directory structure:
```
project/
├── src/                               # Código principal da aplicação
│   ├── core/                          # Configurações e utilitários
│   ├── domain/                        # Entidades e casos de uso (regra de negócio)
│   ├── infra/                         # Banco de dados, repositórios e integrações 
│   ├── presentation/                  # Interfaces de entrada/saída (ex.: FastAPI)
│   └── tests/                         # Testes unitários e de integração
├── pyproject.toml                     # Configuração do Poetry
├── docker-compose.yml                 # Subida do PostgreSQL
└── Makefile                           # Automação de comandos
```
 

### Comandos Básicos

```bash
# Configurar o ambiente de desenvolvimento
make setup

# Iniciar os containers Docker (PostgreSQL)
make up

# Rodar os testes (TDD)
make test

# Derrubar os containers
make down
```

### Conectando ao Banco de Dados

Após executar `make up`, o PostgreSQL estará disponível em:
- Host: localhost
- Porta: 5432
- Usuário: dev
- Senha: dev
- Banco de dados: ecommerce