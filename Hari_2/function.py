from datetime import datetime
def sapa_nama (nama):
    if nama is None:
        print("silakan masukkan nama")
    print (f"halo!{nama}")
sapa_nama()
print(datetime.now())