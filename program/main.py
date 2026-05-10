def main():
    func_log.logging.info(f"INICIANDO.")
    func_sys.start_environment()
    item_list_response = func_steam.getSteamInventory(config.steam_id)
    item_info = func_sys.compileInfo(item_list_response)
    func_sys.moveFile(config.file_name_compiled, config.folder_storage, config.folder_backup)
    func_sys.writeFile(item_info, config.folder_storage, config.file_name_compiled)
    func_log.logging.info(f"FINALIZADO.")

if __name__ == '__main__':
    import config as config
    import functions_logging as func_log
    import functions_system as func_sys
    import functions_steam as func_steam    

    main()