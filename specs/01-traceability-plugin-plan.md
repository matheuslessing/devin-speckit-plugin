# Plano de Arquitetura: Plugin de Rastreabilidade SDD

## Arquitetura Proposta

O repositório será estruturado da seguinte forma:

```text
devin-speckit-plugin/
├── .devin-plugin/
│   └── plugin.json           # Manifesto do plugin
├── AGENTS.md                 # Regras globais injetadas na sessão
├── upstream/                 # [GIT SUBMODULE] Aponta para github/spec-kit
├── scripts/
│   └── build_plugin.py       # Script que extrai do upstream/ e gera a pasta skills/
└── skills/                   # Pasta gerada dinamicamente contendo os prompts
    ├── speckit-specify/
    ├── speckit-plan/
    └── speckit-tasks/
```

## Componentes Chave

1. **Git Submodule (`upstream/`)**
   - Comando de inicialização: `git submodule add https://github.com/github/spec-kit.git upstream`
   - Permite dar `git pull` futuro apenas no código da Microsoft/GitHub para trazer as inovações deles.

2. **Script de Build (`scripts/build_plugin.py`)**
   - Lerá os templates do diretório `upstream/` (como `ARCHITECTURE.md`, exemplos, etc.).
   - Vai formatar as saídas em `SKILL.md` na pasta `skills/` para o Devin ler de forma otimizada.

3. **Manifesto (`plugin.json`)**
   - Vai expor os metadados do plugin e registrar a versão.
