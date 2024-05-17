import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Data Awal
List_Data = []

def show_menu():

    clear_screen()
    print("=== Aplikasi Kontak ===")
    print("[1] Lihat data")
    print("[2] Tambah data")
    print("[3] Edit data")
    print("[4] Hapus data")
    print("[0] Exit")
    print("-----------------------")

    menu = input("Pilih menu : ")

    if menu == '1':
        menu1()
    if menu == '2':
        menu2()
    if menu == '3':
        menu3()
    if menu == '4':
        menu4()
    if menu == '0':
        print("Terimakasih telah berkunjung")
        exit()
    else :
        print("Menu yang anda masukan tidak ada, masukan pilihan yang tersedia!")
        kembali()

def menu1():
    print("NIM || Nama")
    if len (List_Data) <= 0:
        print('Data masih kosong')
    else :
        for data in List_Data :
            print(f"{data [0]} - {data [1]}")
    kembali()

def menu2():
    NIM  = input('Masukan NIM anda : ')
    nama = input('Masukan nama anda : ')
    List_Data.append([NIM, nama])
    print('Data berhasil ditambahkan')
    kembali()

def menu3():
    index = int(input('Masukan nomor index: '))

    nim_baru  = input('Masukan NIM baru: ')
    nama_baru = input('Masukan nama baru: ')
    List_Data[index - 1] = [nim_baru, nama_baru]
    print('nama anda telah dirubah')
    kembali()

def menu4():
    index = int(input('Masukan nomor index: '))
    nama = List_Data[index]
    del List_Data[index]
    print('Data berhasil dihapus')
    kembali()

def kembali():
    print("\n")
    input("Tekan enter untuk kembali")
    show_menu()

while(True) :
    show_menu()
