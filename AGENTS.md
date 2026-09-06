# Constituição do Projeto: Devin Spec-Kit Plugin

## 1. Identidade e Propósito
Este repositório é um plugin nativo para o Devin que encapsula a metodologia e as funcionalidades do `github/spec-kit` oficial. O objetivo é fornecer capacidades de Spec-Driven Development (SDD) para qualquer sessão do Devin que instalar este plugin.

## 2. Rastreabilidade (Traceability)
- O código-fonte fonte da verdade upstream está em `https://github.com/github/spec-kit.git`.
- Atualizações do plugin DEVEM garantir que os prompts e metodologias reflitam os commits mais recentes do upstream.

## 3. Metodologia (Obrigatória)
Qualquer IA operando neste repositório DEVE seguir o Spec-Driven Development:
1. Nenhuma linha de código de feature deve ser escrita sem uma especificação prévia na pasta `specs/`.
2. O ciclo de vida é: `AGENTS.md` -> `specs/*-specification.md` -> `specs/*-plan.md` -> `specs/*-tasks.md` -> Implementação.

## 4. Stack Técnica
- Bash/PowerShell Scripts para orquestração de submodules.
- Python (se necessário para conversão/build).
- JSON/Markdown para o manifesto do Devin Plugin (`.devin-plugin/plugin.json`).
