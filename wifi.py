import os


class MenuStart:
    def __init__(self):
        self.running = True

    def clear_screen(self):
        os.system("clear")

    def run_com(self, command: str):
        os.system(command)

    def on_wifi(self):
        self.run_com("nmcli radio wifi on")

    def off_wifi(self):
        self.run_com("nmcli radio wifi off")

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
            [on wifi]  Turn ON wifi
            [off wifi] Turn OFF wifi
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

            elif choice in {"q", "exit", "end"}:
                self.clear_screen()
                self.running = False
                print("PROGRAM OFF!")
                break

            elif choice == "2":
                self.clear_screen()
                self.run_com("nmcli device status")

            elif choice == "3":
                self.clear_screen()
                self.run_com("nmcli device wifi show-password")

            elif choice == "4":
                try:
                    name_ssid = input("SSID name: ").strip()
                    password = input("Password: ").strip()
                except KeyboardInterrupt:
                    self.clear_screen()
                    continue

                self.run_com(
                    f'nmcli device wifi connect "{name_ssid}" password "{password}"'
                )

            elif choice == "off wifi":
                self.off_wifi()

            elif choice == "on wifi":
                self.on_wifi()

            else:
                print("INVALID OPTION!")


if __name__ == "__main__":
    app = MenuStart()
    app.connected_wifi()