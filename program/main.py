def main():
    func_log.logging.info(f"INICIANDO.")
    utils.start_environment()
    item_list_response = func_steam.getSteamInventory(config.steam_id)
    item_info = utils.compileInfo(item_list_response)
    utils.moveFile(config.file_name_compiled, config.folder_storage, config.folder_backup)
    utils.writeFile(item_info, config.folder_storage, config.file_name_compiled)
    func_log.logging.info(f"FINALIZADO.")

if __name__ == '__main__':
    import config as config
    import program.functions_logging as func_log
    import program.utils as utils
    import program.functions_steam as func_steam    

    main()