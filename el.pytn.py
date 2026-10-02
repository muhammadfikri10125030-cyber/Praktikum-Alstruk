print("Hello dunia")  
def cek_bilangan_prima(angka):
    # Bilangan prima harus lebih besar dari 1
    if angka <= 1:
        return False
    
    # Memeriksa pembagi dari 2 hingga akar dari angka
    for i in range(2, int(angka**0.5) + 1):
        if angka % i == 0:
            return False  # Jika habis dibagi, maka bukan prima
            
    return True  # Jika tidak ada pembagi, maka prima

# Input dari pengguna
try:
    angka_input = int(input("Masukkan sebuah bilangan bulat: "))

    if cek_bilangan_prima(angka_input):
        print(f"{angka_input} adalah bilangan prima.")
    else:
        print(f"{angka_input} BUKAN bilangan prima.")
except ValueError:
    print("Masukkan harus berupa angka bulat!")