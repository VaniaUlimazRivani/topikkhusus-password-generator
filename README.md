# 🔐 Password Generator CLI

CLI tool untuk generate password yang kuat dan aman, dibangun dengan Python.

## ✨ Fitur
- Generate password acak dengan tingkat keamanan tinggi
- Pilih panjang password sesuai kebutuhan
- Generate beberapa password sekaligus
- Indikator kekuatan password (Weak / Medium / Strong)
- Opsi exclude huruf besar, angka, atau simbol
- Copy otomatis ke clipboard

## 🛠️ Tech Stack
- Python 3.x
- `secrets` module (cryptographically secure)
- `argparse` untuk CLI interface
- `pyperclip` untuk clipboard support

## 🚀 Cara Pakai

Install dependency:
\```bash
pip install pyperclip
\```

Jalankan:
\```bash
# Default (16 karakter)
python password_generator.py

# Custom panjang
python password_generator.py -l 24

# Generate 5 password sekaligus
python password_generator.py -n 5

# Tanpa simbol
python password_generator.py --no-symbols

# Copy ke clipboard
python password_generator.py --copy
\```

## 📋 Semua Opsi

| Flag | Deskripsi | Default |
|------|-----------|---------|
| `-l` | Panjang password | 16 |
| `-n` | Jumlah password | 1 |
| `--no-upper` | Tanpa huruf besar | - |
| `--no-digits` | Tanpa angka | - |
| `--no-symbols` | Tanpa simbol | - |
| `--copy` | Copy ke clipboard | - |

## 💡 Kenapa pakai `secrets` bukan `random`?
Module `secrets` dirancang khusus untuk kebutuhan kriptografi dan keamanan,
berbeda dengan `random` yang bisa diprediksi. Ini memastikan password
yang dihasilkan benar-benar tidak bisa ditebak.
