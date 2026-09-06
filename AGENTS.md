# Constituição do Projeto: Devin Spec-Kit Plugin

## 1. Identidade e Propósito
Este repositório é um plugin nativo para o Devin que encapsula a metodologia e as funcionalidades do `github/spec-kit` oficial. O objetivo é fornecer capacidades de Spec-Driven Development (SDD) para qualquer sessão do Devin que instalar este plugin.

## 2. Rastreabilidade (Traceability)
- O código-fonte fonte da verdade upstream está em `https://github.com/github/spec-kit.git`.
- Atualizações do plugin DEVEM garantir que os prompts e metodologias reflitam os commits mais recentes do upstream.

## 3. Metodologia e Triggers (Invocação sob Demanda)
O fluxo de Spec-Driven Development (SDD) é a arquitetura principal deste plugin.

**Gatilho de Chat:** Sempre que o usuário digitar `/sdd` ou frases como `sdd spec driven` no chat, o agente DEVE obrigatoriamente:
1. Executar no terminal o comando `python scripts/drift_check.py` para avaliar o estado atual do repositório.
2. Interromper outras ações e guiar o usuário pelas 3 fases estruturais: Especificação (`specs/*-specification.md`) -> Planejamento (`specs/*-plan.md`) -> Tarefas (`specs/*-tasks.md`).
3. Não escrever código até que as 3 fases estejam aprovadas.

## 4. Stack Técnica
- Bash/PowerShell Scripts para orquestração de submodules.
- Python (se necessário para conversão/build).
- JSON/Markdown para o manifesto do Devin Plugin (`.devin-plugin/plugin.json`).
