# Tarefas (Checklist): Plugin de Rastreabilidade SDD

- [ ] **Fase 1: Configuração do Git e Submodule**
  - [ ] Inicializar repositório Git em `devin-speckit-plugin`.
  - [ ] Adicionar submodule `https://github.com/github/spec-kit.git` na pasta `upstream`.
- [ ] **Fase 2: Geração do Manifesto e Regras**
  - [ ] Criar `.devin-plugin/plugin.json` (Já temos um modelo base, precisa adaptar).
  - [ ] Validar a presença e escopo do `AGENTS.md`.
- [ ] **Fase 3: Automação e Adaptação de Skills**
  - [ ] Criar `scripts/build_plugin.py` para sincronização.
  - [ ] Rodar o script para extrair e montar a pasta `skills/`.
- [ ] **Fase 4: Validação Final**
  - [ ] Executar check de estrutura (simular leitura do Devin).
  - [ ] Entregar comandos Git para o usuário fazer o push final.
