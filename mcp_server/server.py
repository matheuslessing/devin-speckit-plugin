# /// script
# requires-python = ">=3.11"
# dependencies = ["mcp"]
# ///

import subprocess
import os
from mcp.server.fastmcp import FastMCP

# Inicializa o servidor FastMCP
mcp = FastMCP("SpecKitNative")

def run_specify_cmd(args):
    """Executa um comando do spec-kit (specify) isolado na pasta upstream usando uv."""
    try:
        # Resolve path absoluto para a pasta upstream
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        upstream_dir = os.path.join(current_dir, "upstream")

        # Usamos `uv run` para garantir que as dependências do spec-kit sejam
        # resolvidas isoladamente sem poluir o ambiente global do Devin Cloud.
        cmd = ["uv", "run", "--directory", upstream_dir, "python", "-m", "specify"] + args
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Erro ao executar spec-kit: {e.stderr}"
    except Exception as e:
        return f"Erro inesperado no servidor MCP: {str(e)}"

@mcp.tool()
def speckit_search(query: str = "") -> str:
    """Pesquisa catálogos e workflows disponíveis no spec-kit oficial."""
    args = ["bundle", "search"]
    if query:
        args.append(query)
    return run_specify_cmd(args)

@mcp.tool()
def speckit_install(bundle_id: str) -> str:
    """Instala pacotes e workflows do spec-kit no projeto ativo."""
    return run_specify_cmd(["bundle", "install", bundle_id])

@mcp.tool()
def speckit_info(bundle_id: str) -> str:
    """Lê os detalhes de um bundle específico do spec-kit."""
    return run_specify_cmd(["bundle", "info", bundle_id])

@mcp.tool()
def speckit_validate(path: str) -> str:
    """Modo Autor: Valida a integridade estrutural de um bundle local no caminho especificado."""
    return run_specify_cmd(["bundle", "validate", "--path", path])

@mcp.tool()
def speckit_build(path: str) -> str:
    """Modo Autor: Empacota um bundle local no caminho especificado, gerando um arquivo .zip versionado."""
    return run_specify_cmd(["bundle", "build", "--path", path])

if __name__ == "__main__":
    # Roda o servidor usando o protocolo standard (stdio) exigido pelo MCP
    mcp.run()
