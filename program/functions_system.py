import os 
import pandas as pd
from datetime import datetime
import time

import functions_logging as func_log
import config as config
import functions_steam as func_steam

#=======================================================
#FUNÇÕES QUE ADMINISTRAM DIRETÓRIOS, CRIANDO SE NECESSÁRIO
#=======================================================
def start_environment():
    func_log.logging.info("Iniciando ambiente.")
    verifyAndCreateFolderStorage()
    verifyAndCreateFolderBackup()
    verifyAndCreateFolderLog() 
    func_log.logging.info("Inicialização finalizada.")

def verifyAndCreateFolderStorage():
    if not os.path.exists(config.folder_storage):
        os.makedirs(config.folder_storage)

def verifyAndCreateFolderBackup():
    if not os.path.exists(config.folder_backup):
        os.makedirs(config.folder_backup)  

def verifyAndCreateFolderLog():
    if not os.path.exists(config.folder_logs):
        os.makedirs(config.folder_logs)  

#=======================================================
#FUNÇÕES QUE ADMINISTRAM E CRIAM ARQUIVOS DE INFORMAÇÃO
#=======================================================
def moveFile(file_name, curr_path, dest_path):
    list_files = os.listdir(curr_path)
    for file in list_files:
        if file.startswith(file_name.split('_')[0]):
            curr_path = os.path.join(curr_path, file)
            dest_path = os.path.join(dest_path, file)
            os.rename(f"{curr_path}", f"{dest_path}")
            func_log.logging.info(f"Arquivo movimentado. Origem: {curr_path} - Destino: {dest_path}")
        

def writeFile(database, dest_path, file_name):
    df = pd.DataFrame(database)    
    df.to_csv(f"{dest_path}/{file_name}", index=False, sep=';', encoding='utf-8-sig')    
    func_log.logging.info(f"Arquivo criado com sucesso. Diretório: {dest_path}/{file_name}")

#=======================================================
#FUNÇÕES QUE CRIAM E COMPILAM ARQUIVOS DE INFORMAÇÃO
#=======================================================
def compileInfo(item_list_response):
    func_log.logging.info(f"Foram encontrados {len(item_list_response)} itens únicos.")    
    item_info = []

    for item in item_list_response:
        func_log.logging.info(f"Buscando preços...") 
        # A Steam já nos dá o nome oficial em inglês aqui!
        item_name_english = func_steam.getEnglishNameFromResponse(item)
        item_name_portuguese = func_steam.getPortugueseNameFromResponse(item)
        # Filtra itens que não podem ser vendidos (ex: medalhas)
        if item.get('marketable'):
            item_price = func_steam.getItemPrice(item_name_english)
            time.sleep(4) 
        else:
            item_price = 999999

        item_data = {
            "NOME DO ITEM": item_name_portuguese,
            "CÓDIGO DO ITEM": item_name_english,
            "PREÇO ATUAL": item_price
        }
        item_info.append(item_data)
        func_log.logging.info(f"Item: {item_name_portuguese} encontrado.")
    func_log.logging.info(f"Processamento de informações finalizado.")
    return item_info