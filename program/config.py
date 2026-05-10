import os
from datetime import datetime

folder_storage = "storage"
folder_backup = "storage/backup"
folder_logs = "logs"
file_name_compiled = f'compile_{datetime.now().strftime("%Y%m%d%H%M%S")}.csv'
steam_id = '76561198220218819'
country = 'BR'
language='portuguese'
currency = 7 #1=USD, 2=GBP, 3=EUR, 5=RUB, 7=BRL. More currencies: https://partner.steamgames.com/doc/store/pricing/currencies
max_inventory_items = 2
file_name_log = f'{os.getcwd()}/{folder_logs}/log_{datetime.now().strftime("%Y%m%d%H%M%S")}.log'
