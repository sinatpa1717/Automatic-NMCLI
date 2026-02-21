import os

class MenuStart:
    def __init__(self):
        self.running = True

    def clear_screen(self):
        os.system("clear")

    def run_com(self, command: str):
        os.system(command)

    def connected_wifi(self):
        welcome_message = "Hello user\nWelcome to Automatic NMCLI Connected Tool"
        self.clear_screen()
        print(welcome_message.upper().strip())

        while self.running:
            menu_text = """
            ===============
            
            [1] Show list wifi
            [2] Status wifi
            [3] Show password wifi connected
            [4] Connect SSID wifi
            [q] Exit program
            ===============
            """
            print(menu_text.upper())

            try:
                choice = input("----> ").strip().lower()
            except KeyboardInterrupt:
                self.clear_screen()
                self.running = False
                print("PROGRAM OFF!")
                break

            if choice == "1":
                self.clear_screen()
                self.run_com("nmcli device wifi list")

            elif choice in {"q", "exit"}:
                self.clear_screen()
                self.running = False
                print("PROGRAM OFF!")
                break

            else:
                print("INVALID OPTION!")


if __name__ == "__main__":
    app = MenuStart()
    app.connected_wifi()