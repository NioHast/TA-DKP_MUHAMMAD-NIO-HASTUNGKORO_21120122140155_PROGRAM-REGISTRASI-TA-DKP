'''Assalamu'alaikum Wr Wb. Look at the star, look how they shine for you'''

import customtkinter as ctk
import tkinter.messagebox as messagebox

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

# Class (Modul 5)
class Application(ctk.CTk):
    def __init__(self):
        # Constructor (Modul 5)
        super().__init__()
        self.nama_entry = None
        self.nim_entry = None
        self.judul_entry = None
        self.entry1 = None

        self.home_page()

    def home_page(self):
        self.geometry(f"{1000}x{500}")

        self.label1 = ctk.CTkLabel(self, text="Selamat Datang, Praktikan!", font=("Helvetica", 60))
        self.label1.pack(anchor="nw", padx=100, pady=(100, 0))

        self.label2 = ctk.CTkLabel(self, text="Silakan Daftar TA DKP Kalian di sini", font=("Helvetica", 25))
        self.label2.pack(anchor="nw", padx=100, pady=(10, 20))

        self.button1 = ctk.CTkButton(self, text="Daftar", command=self.registration_page)
        self.button1.pack(anchor="nw", padx=100, pady=(10, 20))
        self.button1.configure(width=100, height=30)

    def registration_page(self):
        self.clear_all_widgets()

        self.label1 = ctk.CTkLabel(self, text="Silakan Pilih Asisten Anda", font=("Helvetica", 35))
        self.label1.pack(anchor="nw", padx=35, pady=(25, 0))

        self.label2 = ctk.CTkLabel(self, text="Dan masukkan data diri yang tertera",
                                   font=("Helvetica", 15))
        self.label2.pack(anchor="nw", padx=35, pady=10)

        self.asisten_label = ctk.CTkLabel(self, text="Asisten TA DKP:")
        self.asisten_label.pack()

        self.entry1 = ctk.CTkOptionMenu(self, dynamic_resizing=True, 
                                        values=["Muhammad Irhamsyah Arrahim", "Florencia Irena Amelia", "Muhamad Rafdan Maulana", 
                                                "Refanda Surya Saputra", "Fangki Igo Pramana", "Daffa Abhyasa Santoso",
                                                "Daffa Abhyasa Santoso", "Doan Carlos Embara", "M. Bintang Prayoga Utama",
                                                "Muhammad Raihan Maulana", "Djie Valencia Santoso", "Syahira Isnaeni Dewi", 
                                                "Shinta Nurrohmah", "Yosia Aser Camme", "Farhan Ryan Rafli", "George Miracle Theophylus", 
                                                "Agustinus Adven Christo"])
        self.entry1.pack(padx=25, pady=(0, 15))

        nama_label = ctk.CTkLabel(self, text="Nama:")
        nama_label.pack()

        self.nama_entry = ctk.CTkEntry(self, width=200)
        self.nama_entry.pack()

        nim_label = ctk.CTkLabel(self, text="NIM:")
        nim_label.pack()
        self.nim_entry = ctk.CTkEntry(self, width=200)
        self.nim_entry.pack()

        judul_label = ctk.CTkLabel(self, text="Judul Tugas Akhir:")
        judul_label.pack()
        self.judul_entry = ctk.CTkEntry(self, width=200)
        self.judul_entry.pack()

        submit_button = ctk.CTkButton(self, text="Submit", command=self.validate_entries)
        submit_button.pack(pady=20)

    def validate_entries(self):
        # Getter (Modul 6)
        nama = self.nama_entry.get()
        nim = self.nim_entry.get()
        judul = self.judul_entry.get()
        asisten = self.entry1.get()

        # Pengkondisian (Modul 2)
        if not nama or not nim or not judul or not asisten:
            messagebox.showerror("Error", "Harap isi semua entri.")
        elif not nim.isdigit():
            messagebox.showerror("Error", "NIM harus berisi angka.")
        elif not nama.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Nama harus berisi huruf.")
        elif not judul.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Judul tugas harus berisi huruf.")
        elif not nama.replace(" ", "").isalpha() or not judul.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Nama dan judul tugas harus berisi huruf.")
        else:
            self.ending_page(nama, nim, judul, asisten)

    def ending_page(self, nama, nim, judul, asisten):
        self.clear_all_widgets()

        self.success_frame = ctk.CTkFrame(self, bg_color="white")
        self.success_frame.pack(padx=20, pady=10)

        success_label = ctk.CTkLabel(self.success_frame, text="Selamat, Pendaftaran TA DKP Berhasil!")
        success_label.pack(padx=10, pady=10)

        asisten_label = ctk.CTkLabel(self.success_frame, text="Asisten: " + asisten)
        asisten_label.pack(padx=10, pady=10)

        nama_label = ctk.CTkLabel(self.success_frame, text="Nama: " + nama)
        nama_label.pack(padx=10, pady=10)

        nim_label = ctk.CTkLabel(self.success_frame, text="NIM: " + nim)
        nim_label.pack(padx=10, pady=10)

        judul_label = ctk.CTkLabel(self.success_frame, text="Judul Tugas: " + judul)
        judul_label.pack(padx=10, pady=10)

        back_button = ctk.CTkButton(self, text="Kembali ke Halaman Utama", command=self.go_to_home_page)
        back_button.pack(padx=10, pady=10)

    def go_to_home_page(self):
        self.clear_all_widgets()
        self.home_page()

    def clear_all_widgets(self):
        # Perulangan For (Modul 3)
        for widget in self.winfo_children():
            widget.destroy()

# Pengkondisian (Modul 2)
if __name__ == "__main__":
    app = Application()
    app.mainloop()