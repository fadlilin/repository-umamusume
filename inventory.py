



inventory = {}
max_slot = 18
max_stack = 36

def tambah_barang(nama_barang, jumlah, tipe):
    if nama_barang in inventory:
        if inventory[nama_barang]["jumlah"] + jumlah <= max_stack:
            inventory[nama_barang]["jumlah"] += jumlah
            print(f"{jumlah} {nama_barang} ditambahkan!")
        else:
            print("Stack penuh, tidak bisa menambahkan lagi!")
    else:
        if len(inventory) < max_slot:
            inventory[nama_barang] = {
                "jumlah": jumlah,
                "tipe": tipe
            }
            print(f"{nama_barang} berhasil masuk inventory!")
        else:
            print("Inventory penuh, tidak dapat menambahkan barang!")

def ambil_barang(nama_barang, jumlah):
    if nama_barang in inventory:
        if inventory[nama_barang]["jumlah"] >= jumlah:
            inventory[nama_barang]["jumlah"] -= jumlah
            print(f"{jumlah} {nama_barang} berhasil diambil!")
            if inventory[nama_barang]["jumlah"] == 0:
                del inventory[nama_barang]
        else:
            print("Jumlah barang tidak cukup")
    else:
        print("Barang tidak ada di inventory")

def lihat_inventory():
    if not inventory:
        print("Inventory kosong!")
    else:
        print("\n=== Inventory ===")
        for barang, data in inventory.items():
            print(f"{barang} ({data['tipe']}) : {data['jumlah']}")
        print("=================\n")