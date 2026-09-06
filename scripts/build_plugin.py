import os
import subprocess
import json

def get_upstream_commit():
    """Obtém o hash do último commit do submodule upstream."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"], 
            cwd="upstream", 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Erro ao obter commit do upstream: {e}")
        return "unknown-commit"

def create_skill(name, description, content, commit_hash):
    """Cria o arquivo SKILL.md estruturado para o Devin."""
    skill_dir = os.path.join("skills", name)
    os.makedirs(skill_dir, exist_ok=True)
    
    skill_path = os.path.join(skill_dir, "SKILL.md")
    
    # Injetar rastreabilidade no conteúdo
    full_content = f"""---
name: {name}
description: {description}
---

> **Traceability Note**: Esta skill é baseada na metodologia SDD oficial e foi gerada a partir do upstream github/spec-kit (Commit: `{commit_hash}`).

{content}
"""
    with open(skill_path, "w", encoding="utf-8") as f:
        f.write(full_content)
    print(f"[OK] Skill criada: {name}")

def main():
    print("Iniciando build do Devin Spec-Kit Plugin...")
    commit_hash = get_upstream_commit()
    print(f"Upstream Tracking Commit: {commit_hash}")

    # Skill 1: Specify
    create_skill(
        "speckit-specify",
        "Gera uma especificação estruturada adotando o fluxo SDD.",
        "# spec-kit: Specification\n\nInstruções:\n1. Analise o que o usuário quer construir.\n2. Crie ou atualize `specs/specification.md` com Visão Geral, Requisitos e Cenários de Erro.\n3. Peça aprovação antes de codar.",
        commit_hash
    )

    # Skill 2: Plan
    create_skill(
        "speckit-plan",
        "Cria um plano arquitetural técnico baseado na especificação.",
        "# spec-kit: Planning\n\nInstruções:\n1. Leia `specs/specification.md`.\n2. Crie ou atualize `specs/implementation_plan.md` com Arquitetura, Estruturas de Dados e Dependências.\n3. Peça aprovação.",
        commit_hash
    )

    # Skill 3: Tasks
    create_skill(
        "speckit-tasks",
        "Quebra um plano técnico em tarefas passo a passo.",
        "# spec-kit: Tasks\n\nInstruções:\n1. Leia `specs/implementation_plan.md`.\n2. Crie `specs/task.md` como uma checklist (usando `[ ]`, `[/]`, `[x]`).\n3. Peça autorização para iniciar a execução.",
        commit_hash
    )

    print("Build concluído com sucesso!")

if __name__ == "__main__":
    main()
