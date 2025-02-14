from flask import Flask, render_template, request, jsonify
import pyttsx3

app = Flask(__name__)

# Navbatni yaratish
navbat = []

# Xizmatlarga mos xonalar
xona_haritalar = {
    "kredit xizmati": [28, 29, 30, 31, 32],
    "karta olish": [23, 22, 21, 25, 24, 26],
    "xazna": [1, 2, 3, 4, 5, 6]
}

# Xonalarni boshqarish uchun asl ro‘yxat nusxasi
xona_asosiy = xona_haritalar.copy()

# Ovozli chaqirish funksiyasi
def ovoz_chaqir(raqam, xizmat, xona):
    engine = pyttsx3.init()
    engine.say(f"Navbat raqami {raqam}, iltimos, {xizmat} uchun {xona}-xonga keling!")
    engine.runAndWait()

# Xizmat uchun mos bo‘sh xonani tanlash
def xona_tanla(xizmat):
    xonalar = xona_haritalar.get(xizmat, [])
    if xonalar:
        xona = xonalar.pop(0)  # Bo'sh xonani olish va ro‘yxatdan o‘chirish
        return xona
    return None

# Xizmat tugagach, xonani qayta qo‘shish
def xona_qaytar(xizmat, xona):
    xona_haritalar[xizmat].append(xona)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_to_queue', methods=['POST'])
def add_to_queue():
    ism = request.json.get('ism')
    xizmat = request.json.get('xizmat')

    xona = xona_tanla(xizmat)
    if xona is None:
        return jsonify({"success": False, "message": "Bo'sh xona qolmadi!"})

    navbat.append((ism, xizmat, xona))
    return jsonify({"success": True, "message": f"{ism} navbatga qo'shildi. Xizmat turi: {xizmat}. Xona: {xona}."})

@app.route('/call_from_queue', methods=['POST'])
def call_from_queue():
    if navbat:
        chaqirilgan, xizmat, xona = navbat.pop(0)
        ovoz_chaqir(chaqirilgan, xizmat, xona)
        xona_qaytar(xizmat, xona)  # Xizmatdan so‘ng xonani qaytarish
        return jsonify({"success": True, "message": f"{chaqirilgan} {xizmat} uchun {xona}-xonga chaqirildi."})
    else:
        return jsonify({"success": False, "message": "Navbatda hech kim yo'q."})

@app.route("/view_queue", methods=["GET"])
def view_queue():
    return jsonify({"queue": navbat})

if __name__ == '__main__':
    app.run(debug=True)
