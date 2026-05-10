import requests
import config as config
import functions_logging as func_log

def defineHeader():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    return headers

def getSteamInventory(steam_id):
    func_log.logging.info(f"Definindo URL para o usuário: {steam_id}")

    url = f"https://steamcommunity.com/inventory/{steam_id}/730/2"
    func_log.logging.info(f"URL definida com sucesso! - {url}")
    
    # Parâmetros da requisição
    params = {
        'l': 'portuguese',
        'count': config.max_inventory_items 
    }

    # Simula um navegador real
    headers = defineHeader()

    try:
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code != 200:
            func_log.logging.error(f"Erro {response.status_code}: {response.text}") 
            return None
        
        data = response.json()
        
        if not data or 'descriptions' not in data:
            func_log.logging.error(f"Inventário vazio ou privado.")
            return None
            
        return data['descriptions']

    except Exception as e:
        func_log.logging.error(f"Erro na conexão: {e}")
        return None

def getItemPrice(item):
    url = "https://steamcommunity.com/market/priceoverview/"
    
    # O requests vai codificar o market_hash_name automaticamente na URL
    query_params = {
        'country': 'BR',
        'currency': 7,
        'appid': 730,
        'market_hash_name': item
    }

    headers = defineHeader()

    try:
        # Passamos os parâmetros e os cabeçalhos
        response = requests.get(url, params=query_params, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                return data.get('lowest_price', 'Sem preço')
            
            func_log.logging.warning(f"Preço não encontrado para o item {item}")
            return -1
        
        elif response.status_code == 429:
            func_log.logging.error("Erro 429: Muita pressa! Steam bloqueou temporariamente.")
            return -2
        
        else:
            func_log.logging.error(f"Erro {response.status_code}")
            return 

    except Exception as e:
        func_log.logging.error(f"Erro na requisição: {e}")
        return 
    
def getEnglishNameFromResponse(item_response):
    name_en = item_response['market_hash_name']
    return name_en

def getPortugueseNameFromResponse(item_response):
    name_pt = item_response['name']
    return name_pt