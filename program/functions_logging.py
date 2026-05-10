import logging
import os
import config as config

def get_logger(logger_name):
    # Configuração básica
    if not os.path.exists(config.folder_logs):
        os.makedirs(config.folder_logs)  

    logging.basicConfig(
        filename=config.file_name_log, 
        level=logging.INFO, 
        filemode='w',
        encoding = 'utf-8',
        format = "'%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'")

    logger = logging.getLogger(logger_name)
    Stream_Handler = logging.StreamHandler()
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    Stream_Handler.setFormatter(formatter)
    logger.addHandler(Stream_Handler)

    return logger

logging = get_logger(__name__)

# logging.debug("Mensagem de depuração (geralmente oculta)")
# logging.info("Informação geral de execução")
# logging.warning("Um aviso que algo inesperado ocorreu")
# logging.error("Um erro ocorreu, mas o programa continua")
# logging.critical("Erro grave que interrompe o programa")