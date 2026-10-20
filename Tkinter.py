import tkinter as tk
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("350x500")

label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Times New Roman", 14, "bold"))
label_judul.grid(row=0, column=0, columnspan=2, pady=15)


mata_pelajaran = [
    "Matematika", "Fisika", "Kimia", "Biologi", 
    "Bahasa Indonesia", "Bahasa Inggris", "Informatika", 
    "Sejarah", "Ekonomi", "Sosiologi"
]

entries = []
for i, mapel in enumerate(mata_pelajaran):
    lbl = tk.Label(
        root, 
        text=f"Nilai {mapel}:", 
        font=("Times New Roman", 10, "bold"), 
        fg="#00050C"
    )
    lbl.grid(row=i+1, column=0, padx=30, pady=3, sticky="w")

    entry = tk.Entry(root, width=15, font=("Times New Roman", 10), bd=2, relief="groove")
    entry.grid(row=i+1, column=1, padx=30, pady=3)
    entries.append(entry)

def prediksi_prodi():
    label_hasil.config(text="Hasil Prediksi: Teknologi Informasi")
    
btn_prediksi = tk.Button(root, text="Hasil Prediksi", command=prediksi_prodi)
btn_prediksi.grid(row=11, column=0, columnspan=2, pady=10)
    
root.mainloop()