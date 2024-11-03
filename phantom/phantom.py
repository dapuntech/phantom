import ui.ui_info as ui_info

if __name__ == "__main__":
    ui_info.menu_banner()
    try:
        while True:
            input_data = input("enter your choice: ")
            if input_data == "1":
                ui_info.available_tool()
                ui_info.menu_info()
            if input_data == "2":
                ui_info.install_tool()
                ui_info.menu_info()
    except KeyboardInterrupt:
        print("\nexiting...")
