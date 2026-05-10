import time
import os
import config as config
#import functions_logging as func_log
import functions_steam as func_steam

# item_list_response = func_steam.getSteamInventory(config.steam_id)

# for item in item_list:
#     price = func_steam.getItemPrice(item)
#     print(f"{item}: {price}")
#     # Pausa de 3 segundos entre itens para evitar bloqueio de IP (Rate Limit)
#     time.sleep(3)


file_name_compiled = f'compile_20260101.csv'
print(file_name_compiled.split('_')[0])