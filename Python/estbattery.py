# Formula = mAh ÷ mA * 0.7 = estmated hours

import subprocess
import time

class EstBattery:
    def banner(self):
        subprocess.call("clear")
        print("\n    ╔════════════════╗")
        print("    ║████████████████╚╗")
        print("    ║████ Est Bat ███ ║")
        print("    ║████████████████╔╝")
        print("    ╚════════════════╝\n")
        print(" - Estimated Battery life - \n")

    def est_battery(self):
        print("Enter the following information: ")
        time.sleep(1.5)
        self.banner()
        battery_capacity = int(input('[+] Battery Capacity(mAh): '))
        device_consumption = int(input('[+] Current Load(mA): '))
        formular = (battery_capacity / device_consumption * 0.7)
        estimated_life = str(formular)
        estimated_days = str(round(formular / 24, 1))
        print("[+] Estimated battery life is {} hours.".format(estimated_life))
        if formular > 24:
            print("[+] Estimated battery life is {} days.\n".format(estimated_days))

    def main(self):
        self.banner()
        self.est_battery()

if __name__ == '__main__':
    estbattery = EstBattery()
    estbattery.main()