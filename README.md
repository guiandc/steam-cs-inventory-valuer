python main.py
   Compreendido. Aqui está o conteúdo completo em um único bloco de código, formatado para que você possa copiar tudo de uma vez e colar diretamente no seu arquivo `README.md`.
```markdown
# Steam CS Inventory Valuer 🎮💰

O **Steam CS Inventory Valuer** é uma ferramenta em Python desenvolvida para automatizar a leitura de inventários de Counter-Strike (CS2) e calcular o valor de mercado dos itens em tempo real. 

O projeto foca em modularidade, utilizando bibliotecas robustas de análise de dados e seguindo padrões de arquitetura limpa para facilitar a manutenção e escalabilidade.

## 🚀 Funcionalidades
*   **Consulta de Inventário:** Integração com a API pública da Steam para listagem de itens.
*   **Valoração em Tempo Real:** Busca preços atualizados no Mercado da Comunidade Steam.
*   **Análise de Dados:** Utiliza Pandas e Numpy para processamento eficiente das informações coletadas.
*   **Internacionalização:** Suporte a diferentes moedas e idiomas via arquivo de configuração.
*   **Gestão de Logs:** Sistema de rastreamento com rotação diária para monitoramento de execução.
*   **Sistema de Arquivos Automático:** Criação dinâmica de diretórios para logs e armazenamento via utilitários dedicados (utils).

## 🛠️ Tecnologias
*   **Python 3.x**
*   **Pandas & Numpy:** Para manipulação e análise de dados.
*   **Requests:** Para comunicação com as APIs da Steam.
*   **Logging:** Para diagnóstico e histórico de operações.

## 📂 Estrutura do Projeto
*   `main.py`: Ponto de entrada que coordena a execução do script.
*   `config.py`: Centraliza variáveis de ambiente como `STEAM_ID`, `CURRENCY` e `LANGUAGE`.
*   `utils.py`: Funções utilitárias (ex: abstração de criação de diretórios).
*   `func_log.py`: Configuração e inicialização do sistema de logs em UTF-8.
*   `requirements.txt`: Gerenciador de dependências do projeto.
*   `logs/`: Armazenamento de registros de execução (ignorado pelo Git).
*   `storage/`: Destino de arquivos CSV e backups (ignorado pelo Git).

## 🔧 Instalação e Uso

1. **Clone o repositório e acesse a pasta:**
   git clone https://github.com/guiandc/steam-cs-inventory-valuer.git
   cd steam-cs-inventory-valuer

2. **Instale as dependências via requirements:**
    pip install -r requirements.txt

3. **Configure seus dados:**
    Abra o arquivo config.py, insira o seu STEAM_ID e ajuste os parâmetros de LANGUAGE e CURRENCY se necessário.

4. **Execute o script:**
    python main.py


📝 Padrões de Desenvolvimento
O projeto adota a convenção de Conventional Commits:

feat: Novas funcionalidades.

fix: Correções de bugs.

refactor: Melhorias no código sem alteração de funcionalidade.

docs: Atualizações na documentação.

Desenvolvido por Guilherme