# Steam CS Inventory Valuer 🎮💰

Script em Python projetado para ler o inventário de Counter-Strike (CS2) de um usuário via SteamID64 e consultar os preços atuais de mercado em Reais (BRL). Ideal para monitorar o valor de coleções de skins e itens comercializáveis.

## 🚀 Funcionalidades
*   **Leitura de Inventário:** Integração com a API pública de inventários da Steam.
*   **Conversão de Moeda:** Busca de preços diretamente em BRL (R$).
*   **Logging Robusto:** Sistema de logs com rotação diária e tratamento de caracteres especiais (UTF-8).
*   **Prevenção de Bloqueio:** Implementação de headers (User-Agent) e intervalos (delay) para respeitar o Rate Limit da Steam.

## 🛠️ Tecnologias Utilizadas
*   [Python 3.9+](https://www.python.org/)
*   [Requests](https://psf.github.io/requests/) - Para chamadas de API.
*   [Logging](https://docs.python.org/3/library/logging.html) - Para rastreamento de eventos e erros.

## 📋 Pré-requisitos
Antes de começar, você precisará:
1.  **SteamID64:** O ID de 17 dígitos do perfil.
2.  **Perfil Público:** O inventário da conta deve estar configurado como "Público" nas configurações de privacidade da Steam.

## 🔧 Instalação e Uso

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/guiandc/steam-cs-inventory-valuer.git](https://github.com/guiandc/steam-cs-inventory-valuer.git)
   cd steam-cs-inventory-valuer