import os 
from cli import *
from terminal.outputs import tampilkan_pilihan

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def kumpulan_menu():
    while True:
        cls()
        tampilkan_pilihan()

        pilihan = input("Pilihan: ")
        cls()

        if pilihan == "1":
            menu_biodata()
        elif pilihan == "2":
            input_sks_cli()
            input("")
        elif pilihan == "3":
            input_nilai()
            input("")
        elif pilihan == "4":
            lihat_nilai()
            input("")
        elif pilihan == "5":
            hitung_ip_cli()
            input("")
        elif pilihan == "6":
            print("Program selesai")
            break
        else:
            print("Pilihan tidak valid")
            input("")