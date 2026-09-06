# Especificação: Modo Autor (MCP) e Lifecycle Hooks

## Visão Geral
Expandir o `devin-speckit-plugin` para não ser apenas um consumidor, mas um criador de workflows. Adicionalmente, proteger o fluxo de trabalho (SDD) através de verificações automatizadas de ciclo de vida (Hooks).

## Requisitos Funcionais
1. **MCP Autor:** O Servidor MCP deve suportar as tools `speckit_validate` e `speckit_build`, permitindo que a IA construa e empacote novos bundles do Spec-Kit.
2. **Lifecycle Hooks:** Implementar um gatilho `UserPromptSubmit` (valido no Cloud) que execute uma verificação rápida para garantir que a pasta `specs/` existe e não está vazia.

## Requisitos Não Funcionais
- O hook de validação deve ser não-obstrutivo (não deve bloquear a sessão, apenas registrar o aviso no console do agente).
