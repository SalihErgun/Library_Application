import json

# Kitapları JSON dosyasından okuma
def read_books():
    try:
        with open("kitap.json", "r", encoding="utf-8") as file:
            kitaplar = json.load(file)
    except FileNotFoundError:
        kitaplar = []  # Dosya yoksa boş bir liste döndür
    return kitaplar

# Kitapları JSON dosyasına yazma
def write_books(kitaplar):
    with open("kitap.json", "w", encoding="utf-8") as file:
        json.dump(kitaplar, file, ensure_ascii=False, indent=4)

# Kitap bilgilerini ekrana yazdırma (strip boşluk karakterlerinden temizleme)
def print_books():
    kitaplar = read_books()  # Kitapları oku
    for kitap in kitaplar:
        # Eğer anahtarların sonunda boşluk veya yeni satır karakteri varsa, temizleyin
        for key in kitap.keys():
            kitap[key] = kitap[key].strip() if isinstance(kitap[key], str) else kitap[key]
        
        # Dil ve Fiyat için boş kontrolü (get kullanarak anahtarın var olup olmadığını kontrol etme)
        dil = kitap.get("Dil", "Bilinmiyor")
        fiyat = kitap.get("Fiyat", "Bilinmiyor")
        barkod = kitap.get("Barkod", "Bilinmiyor")
        
        print(barkod)  # Barkod
        print(kitap["Kitap_Adi"])  # Kitap adı
        print(kitap["Yazar"])  # Yazar
        print(fiyat)  # Fiyat
        print(dil)  # Dil
        print(kitap["Yayinevi"])  # Yayinevi
        print("-" * 20)  # Her kitap arasına bir ayraç ekleyelim

# 1. ADD BOOK (Kitap Ekleme)
def add_book():
    kitaplar = read_books()  # Kitapları oku
    barkod = input("Barkod numarasını girin: ")
    kitap_adi = input("Kitap adını girin: ")
    yazar = input("Yazar adını girin: ")
    fiyat = input("Fiyatı girin: ")
    dil = input("Dili girin: ")
    yayinevi = input("Yayınevi adını girin: ")

    # Yeni kitap sözlüğü
    yeni_kitap = {
        "Barkod": barkod,
        "Kitap_Adi": kitap_adi,
        "Yazar": yazar,
        "Fiyat": fiyat,
        "Dil": dil,
        "Yayinevi": yayinevi
    }

    # Kitapları listeye ekle ve dosyaya yaz
    kitaplar.append(yeni_kitap)
    write_books(kitaplar)
    print("Kitap başarıyla eklendi.")

# 2. SEARCH BOOK (Kitap Arama)
def search_book():
    kitaplar = read_books()  # Kitapları oku
    arama_kriteri = input("Arama yapmak için bir kitap adı, yazar veya barkod girin: ")

    # Arama sonuçları
    bulunan_kitaplar = [kitap for kitap in kitaplar if arama_kriteri.lower() in kitap["Kitap_Adi"].lower() or arama_kriteri.lower() in kitap["Yazar"].lower() or arama_kriteri in str(kitap["Barkod"])]
    
    if bulunan_kitaplar:
        for kitap in bulunan_kitaplar:
            print("-" * 20)
            print(f"Barkod: {kitap['Barkod']}")
            print(f"Kitap Adı: {kitap['Kitap_Adi']}")
            print(f"Yazar: {kitap['Yazar']}")

            # 'Fiyat' ve 'Dil' anahtarlarını kontrol et
            fiyat = kitap.get('Fiyat', 'Bilinmiyor')  # Eğer 'Fiyat' yoksa 'Bilinmiyor' yazdır
            dil = kitap.get('Dil', 'Bilinmiyor')  # Eğer 'Dil' yoksa 'Bilinmiyor' yazdır

            print(f"Fiyat: {fiyat}")
            print(f"Dil: {dil}")
            print(f"Yayınevi: {kitap['Yayinevi']}")
            print("-" * 20)
    else:
        print("Aradığınız kriterlere uygun kitap bulunamadı.")


# 3. DELETE BOOK (Kitap Silme)
def delete_book():
    kitaplar = read_books()  # Kitapları oku
    barkod = input("Silmek istediğiniz kitabın barkod numarasını girin: ")

    # Barkod numarasına göre kitap bul
    kitaplar = [kitap for kitap in kitaplar if kitap["Barkod"] != barkod]

    # Kitapları güncel dosyaya yaz
    write_books(kitaplar)
    print("Kitap başarıyla silindi.")
