# Plano Arquitetural: Modo Autor e Hooks

## Componentes a serem desenvolvidos

1. **`.devin-plugin/hooks.json`**:
   - Registrar um listener para o evento `UserPromptSubmit`.
   - Ação: Invocar `python scripts/drift_check.py`.

2. **`scripts/drift_check.py`**:
   - Script ultraleve.
   - Analisa a raiz do repositório em busca do diretório `specs/`.
   - Retorna um Warning no stdio se os desenvolvedores/IA tentarem programar sem artefatos de especificação.

3. **`mcp_server/server.py` (Expansão)**:
   - Adicionar `@mcp.tool()` para `validate --path <path>`.
   - Adicionar `@mcp.tool()` para `build --path <path>`.
