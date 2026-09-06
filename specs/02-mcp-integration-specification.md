# Especificação: Integração MCP Nível 2 (O Estado da Arte)

## Visão Geral
Elevar o `devin-speckit-plugin` ao nível máximo de extensibilidade, embutindo um Servidor MCP (Model Context Protocol) diretamente no plugin. Isso permitirá que o Devin Cloud opere as ferramentas nativas do repositório `upstream` (github/spec-kit) como se fossem comandos internos da sua própria IA.

## Decisão Arquitetural (In-Plugin vs Custom Cloud)
Como verdadeiros engenheiros, optamos por **empacotar o MCP dentro do Plugin**. A documentação oficial do Devin garante que plugins suportam o arquivo `.mcp.json`. Isso zera o atrito: quem instala o plugin ganha o servidor MCP automaticamente, sem precisar ir no painel da nuvem configurar endpoints customizados.

## Requisitos Funcionais
O Servidor MCP deve expor as seguintes Tools (Ferramentas) para a IA do Devin:
1. `speckit_bundle_search`: Permite ao Devin pesquisar catálogos e workflows disponíveis no spec-kit.
2. `speckit_bundle_info`: Permite ao Devin ler os detalhes de um bundle.
3. `speckit_bundle_install`: Permite ao Devin instalar pacotes do spec-kit no projeto ativo.

## Requisitos Não Funcionais
1. **Zero-Dependency Hard Setup:** O servidor MCP será escrito em Python padrão e fará a ponte direta com o código na pasta `upstream/`, garantindo que não quebre a sessão do Devin.
