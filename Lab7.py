class Mahasiswa:
    def __init__(self):
        self.daftar_mahasiswa = []
    
    def tambah(self):
        """Method untuk menambah data mahasiswa"""
        print("\n=== Tambah Data Mahasiswa ===")
        nama = input("Masukkan nama mahasiswa: ")
        try:
            nilai = float(input("Masukkan nilai mahasiswa: "))
            self.daftar_mahasiswa.append({"nama": nama, "nilai": nilai})
            print(f"Data {nama} berhasil ditambahkan!")
        except ValueError:
            print("Nilai harus berupa angka!")
    
    def tampilkan(self):
        """Method untuk menampilkan semua data mahasiswa"""
        print("\n=== Daftar Nilai Mahasiswa ===")
        if not self.daftar_mahasiswa:
            print("Belum ada data mahasiswa.")
        else:
            print(f"{'No':<5} {'Nama':<20} {'Nilai':<10}")
            print("-" * 35)
            for i, mhs in enumerate(self.daftar_mahasiswa, 1):
                print(f"{i:<5} {mhs['nama']:<20} {mhs['nilai']:<10}")
    
    def hapus(self, nama):
        """Method untuk menghapus data berdasarkan nama"""
        for mhs in self.daftar_mahasiswa:
            if mhs['nama'].lower() == nama.lower():
                self.daftar_mahasiswa.remove(mhs)
                print(f"Data {nama} berhasil dihapus!")
                return
        print(f"Data dengan nama {nama} tidak ditemukan!")
    
    def ubah(self, nama):
        """Method untuk mengubah data berdasarkan nama"""
        for mhs in self.daftar_mahasiswa:
            if mhs['nama'].lower() == nama.lower():
                try:
                    nilai_baru = float(input(f"Masukkan nilai baru untuk {nama}: "))
                    mhs['nilai'] = nilai_baru
                    print(f"Data {nama} berhasil diubah!")
                    return
                except ValueError:
                    print("Nilai harus berupa angka!")
                    return
        print(f"Data dengan nama {nama} tidak ditemukan!")


def main():
    sistem = Mahasiswa()
    
    while True:
        print("\n" + "="*40)
        print("SISTEM MANAJEMEN NILAI MAHASISWA")
        print("="*40)
        print("1. Tambah data mahasiswa")
        print("2. Tampilkan semua data")
        print("3. Hapus data mahasiswa")
        print("4. Ubah data mahasiswa")
        print("5. Keluar")
        print("="*40)
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            sistem.tambah()
        elif pilihan == "2":
            sistem.tampilkan()
        elif pilihan == "3":
            nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
            sistem.hapus(nama)
        elif pilihan == "4":
            nama = input("Masukkan nama mahasiswa yang akan diubah: ")
            sistem.ubah(nama)
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1-5.")


if __name__ == "__main__":
    main()
