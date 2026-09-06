# Plano de Arquitetura: Servidor MCP Integrado

## Arquitetura Proposta

Vamos adicionar a camada de rede do MCP à árvore do nosso plugin:

```text
devin-speckit-plugin/
├── .devin-plugin/
│   └── plugin.json
├── .mcp.json                 <-- NOVO: O Devin lerá isso ao iniciar a sessão
├── AGENTS.md
├── mcp_server/               <-- NOVO: Código do servidor
│   └── server.py             <-- Script que atua sobre protocolo stdio (MCP padrão)
└── upstream/                 <-- (Nosso código fonte original)
```

## Componentes Chave

1. **O Arquivo `.mcp.json`:**
   Este arquivo na raiz do repositório é o padrão oficial. Ele instrui o Devin a subir um processo em background quando o plugin for instalado:
   ```json
   {
     "mcpServers": {
       "speckit-native": {
         "command": "python",
         "args": ["mcp_server/server.py"]
       }
     }
   }
   ```

2. **O Servidor `server.py`:**
   Em vez de forçar instalações complexas (já que dispensamos o hook), vamos escrever um servidor MCP que se comunica via *Standard Input/Output* (`stdio`). Quando o Devin pedir para rodar a tool `speckit_bundle_search`, o servidor traduz isso para uma chamada `subprocess.run()` rodando o código Python que já vive dentro da nossa pasta `upstream/`. Isso isola e protege a execução.
