def temukan_no_telepon(nama, buku_telepon):
    for entry in buku_telepon:
        if entry[0] == nama:
            return entry[1]
    return None

# Buku telepon
buku_telepon = [
    ["John Doe", "081234567890"],
    ["Jane Smith", "089876543210"],
    ["Michael Johnson", "087811223344"],
    ["Emily Davis", "082122232425"]
]

# Mencari nomor telepon Jane
nama = "Jane Smith"
no_telepon = temukan_no_telepon(nama, buku_telepon)

# Menampilkan nomor telepon Jane
if no_telepon:
    print("Nomor telepon", nama, "adalah", no_telepon)
else:
    print("Nomor telepon", nama, "tidak ditemukan")