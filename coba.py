tujuan = input("Masukkan kota : ")
berat_barang = int(input("Masukkan berat barang :"))

if tujuan == "bandung":
    if 0 < berat_barang < 50:
        print("Biaya pengiriman = Rp. 75.000")
    elif berat_barang >= 50 and berat_barang <= 100:
        print("Biaya pengiriman = Rp. 60.000")
    elif berat_barang > 100:
        print("Biaya pengiriman = Rp. 100.000")
    else:
        print("berat tidak boleh -")
elif tujuan == "palembang":
    if 0 < berat_barang < 50:
        print("Biaya pengiriman = Rp. 200.000")
    elif berat_barang >= 50 and berat_barang <= 100:
        print("Biaya pengiriman = Rp. 250.000")
    elif berat_barang > 100:
        print("Biaya pengiriman = Rp. 230.000")
    else:
        print("berat tidak boleh -")
else:
    print("tujuan tidak ditemukan")