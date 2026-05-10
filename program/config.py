import os
from datetime import datetime

folder_storage = "storage"
folder_backup = "storage/backup"
folder_logs = "logs"
file_name_compiled = f'compile_{datetime.now().strftime("%Y%m%d%H%M%S")}.csv'
steam_id = '76561198220218819'
max_inventory_items = 100
file_name_log = f'{os.getcwd()}/{folder_logs}/log_{datetime.now().strftime("%Y%m%d%H%M%S")}.log'
