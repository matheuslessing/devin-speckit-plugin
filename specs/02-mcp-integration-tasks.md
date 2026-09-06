# Tarefas (Checklist): Integração MCP Integrado

- [ ] **Fase 1: Configuração do Motor MCP**
  - [ ] Criar o arquivo `.mcp.json` na raiz do plugin.
  - [ ] Criar a pasta `mcp_server/`.
- [ ] **Fase 2: Desenvolvimento do Servidor (Python)**
  - [ ] Escrever `server.py` implementando o protocolo MCP sobre STDIO.
  - [ ] Adicionar o handler (ferramenta) `speckit_search`.
  - [ ] Adicionar o handler (ferramenta) `speckit_install`.
- [ ] **Fase 3: Refatoração de Metadados**
  - [ ] Atualizar o `.devin-plugin/plugin.json` mencionando a nova capacidade ativa via MCP.
- [ ] **Fase 4: Deploy**
  - [ ] Fazer commit no repositório.
  - [ ] Dar push para o GitHub (`matheuslessing/devin-speckit-plugin`).
