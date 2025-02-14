import pyttsx3

# Navbatni yaratish
navbat = []

# Ovozli chaqirish funksiyasi
def ovoz_chaqir(raqam):
    engine = pyttsx3.init()
    engine.say(f"Navbat raqami {raqam}, iltimos, keling!")
    engine.runAndWait()

# Foydalanuvchini navbatga qo'shish
def navbatga_qosh(ism):
    navbat.append(ism)
    print(f"{ism} navbatga qo'shildi. Navbat raqami: {len(navbat)}")

# Navbatdan chaqirish
def navbat_chaqir():
    if navbat:
        chaqirilgan = navbat.pop(0)
        print(f"{chaqirilgan} chaqirildi.")
        ovoz_chaqir(chaqirilgan)
    else:
        print("Navbatda hech kim yo'q.")

# Tizimni boshqarish
while True:
    print("\n1. Navbatga qo'shish")
    print("2. Navbatdan chaqirish")
    print("3. Chiqish")
    tanlov = input("Tanlang: ")

    if tanlov == '1':
        ism = input("Ism yoki raqam kiriting: ")
        navbatga_qosh(ism)
    elif tanlov == '2':
        navbat_chaqir()
    elif tanlov == '3':
        print("Tizim tugatildi.")
        break
    else:
        print("Noto'g'ri tanlov, qayta urinib ko'ring.")
