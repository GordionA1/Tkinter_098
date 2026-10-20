import tkinter as tk
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("450x600")

root.configure(bg="#023051")

label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Times New Roman", 14, "bold"))
label_judul.grid(row=0, column=0, columnspan=2, pady=15)


mata_pelajaran = [
    "Matematika", "Fisika", "Kimia", "Biologi", 
    "Bahasa Indonesia", "Bahasa Inggris", "Informatika", 
    "Sejarah", "Ekonomi", "Sosiologi"
]

root.mainloop()