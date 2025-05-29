from flask import Flask, render_template, url_for, request, session, redirect
import requests
import csv
import os
import sqlite3
import json
import xmltodict
import yaml
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "manaatslega"

# ========================== Datubāzes inicializācija ==========================
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lietotaji (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vards TEXT NOT NULL,
            dzimums TEXT NOT NULL,
            hobijs TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS administratori (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lietotajvards TEXT NOT NULL,
            parole TEXT NOT NULL
        )
    ''')
    cursor.execute('SELECT * FROM administratori WHERE lietotajvards = ?', ('admin',))
    if not cursor.fetchone():
        cursor.execute('INSERT INTO administratori (lietotajvards, parole) VALUES (?,?)',
                       ('admin', generate_password_hash('admin')))
    conn.commit()
    conn.close()

init_db()

# ========================== Routing ==========================
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/par_mums')
def par_mums():
    return render_template("par_mums.html")

@app.route('/kontakti')
def kontakti():
    return render_template("kontakti.html")

@app.route('/pamati_sintakse')
def pamati_sintakse():
    return render_template("pamati_sintakse.html")

@app.route('/sveiciens')
def sveiciens():
    return render_template("sveiciens.html")

@app.route('/mainigie')
def mainigie():
    vards = "Igors"
    vecums = 35
    skaitlis1 = 4
    skaitlis2 = 7
    summa = skaitlis1 + skaitlis2
    return render_template("mainigie.html", viens=skaitlis1, divi=skaitlis2,
                           vards=vards, vecums=vecums, summa=summa)

@app.route('/datu_tipi')
def datu_tipi():
    teksts = "Sveicieni! Šis ir teksts"
    skaitlis = 100
    decimals = 10.5
    saraksts = ["vards", 2, 3, 4, 5]
    mans_dict = {"vards": "Anna", "vecums": 20}
    mans_kopa = {1, 2, 3, 4, 5}
    return render_template("datu_tipi.html", teksts=teksts, skaitlis=skaitlis,
                           decimals=decimals, saraksts=saraksts, mans_dict=mans_dict,
                           mans_kopa=mans_kopa)

@app.route('/operatori')
def operatori():
    a = 13
    b = 13
    return render_template("operatori.html",
                           summa=a + b,
                           starpiba=a - b,
                           reizinajums=a * b,
                           dalijums=a / b,
                           atlikums=a % b,
                           vienads=(a == b))

@app.route('/kontroles_strukturas')
def kontroles_strukturas():
    x = 4
    rezultats = "Ir tādi darbinieki" if 40 <= x <= 50 else "Neatbilst"
    for_cikls_rezultats = list(range(1, 11))
    while_cikla_rezultats = []
    y = 0
    while y <= 5:
        while_cikla_rezultats.append(y)
        y += 2
    return render_template('kontroles_strukturas.html', rezultats=rezultats,
                           for_cikls_rezultats=for_cikls_rezultats,
                           while_cikla_rezultats=while_cikla_rezultats)

@app.route('/funkcijas')
def funkcijas():
    def sveiciens(vards="Pēteris", uzvards="Bērzs"):
        return f"Sveiks {vards} {uzvards}!"
    return render_template('funkcijas.html',
                           noklusejuma_sveiciens=sveiciens(),
                           izmainitais_sveiciens=sveiciens("Vilips", "Zariņš"))

@app.route('/ievade_izvade', methods=['GET', 'POST'])
def ievade_izvade():
    vards = request.form['vards'] if request.method == 'POST' else None
    return render_template('ievade_izvade.html', vards=vards)

@app.route('/failu_apstrade')
def failu_apstrade():
    try:
        with open('piemers.txt', 'r') as fails:
            saturs = fails.read()
    except IOError:
        saturs = "Fails nav atrasts!"
    return render_template("failu_apstrade.html", saturs=saturs)

@app.route('/oop')
def oop():
    class Persona:
        def __init__(self, vards, vecums):
            self.vards = vards
            self.vecums = vecums

        def sveiciens(self):
            return f"Sveiki, mani sauc {self.vards} un mans vecums ir {self.vecums} gadi."
    persona1 = Persona("Janis", 30)
    persona2 = Persona("Anna", 21)
    return render_template("oop.html", sveiciens=persona1.sveiciens(),
                           sveiciens2=persona2.sveiciens())

@app.route('/moduli')
def moduli():
    import math
    return render_template("moduli.html", summa=math.sqrt(16) + math.pow(16, 2))

@app.route('/joks')
def joks():
    atbilde = requests.get('https://api.chucknorris.io/jokes/random')
    dati = atbilde.json()
    return render_template("json.html", joks=dati['value'],
                           adrese=dati['url'], avatars=dati['icon_url'])

@app.route('/aptauja')
def aptauja():
    return render_template("aptauja.html")

@app.route('/iesniegt', methods=['GET', 'POST'])
def iesniegt():
    if request.method == 'POST':
        vards = request.form['vards']
        dzimums = request.form['dzimums']
        hobiji_str = ', '.join(request.form.getlist('hobiji'))
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO lietotaji (vards, dzimums, hobijs) VALUES (?,?,?)',
                       (vards, dzimums, hobiji_str))
        conn.commit()
        conn.close()
        return render_template('paldies.html')
    return redirect(url_for('aptauja'))

@app.route('/pieteikties', methods=['GET', 'POST'])
def pieteikties():
    if request.method == 'POST':
        lietotajvards = request.form['lietotajvards']
        parole = request.form['parole']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM administratori WHERE lietotajvards = ?', (lietotajvards,))
        admin = cursor.fetchone()
        conn.close()
        if admin and check_password_hash(admin[2], parole):
            session['lietotajvards'] = lietotajvards
            return redirect(url_for('panelis'))
    return render_template('pieteikties.html')

@app.route('/panelis')
def panelis():
    if 'lietotajvards' not in session:
        return redirect(url_for('pieteikties'))
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM lietotaji')
    lietotaji = cursor.fetchall()
    conn.close()
    return render_template('panelis.html', lietotaji=lietotaji)

@app.route('/dzest/<int:id>')
def dzest_lietotaju(id):
    if 'lietotajvards' not in session:
        return redirect(url_for('pieteikties'))
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM lietotaji WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('panelis'))

@app.route('/dzest2/<string:vards>')
def dzest_rindu_csv(vards):
    jauni_dati = []
    with open('dati.csv', newline='', encoding='utf-8') as csvfails:
        lasitajs = csv.reader(csvfails)
        for rinda in lasitajs:
            if rinda[0] != vards:
                jauni_dati.append(rinda)
    with open('dati.csv', 'w', newline='', encoding='utf-8') as csvfails:
        rakstitajs = csv.writer(csvfails)
        rakstitajs.writerows(jauni_dati)
    return redirect(url_for('csv_skats'))

@app.route('/izlogoties')
def izlogoties():
    session.pop('lietotajvards', None)
    return redirect(url_for('pieteikties'))

@app.route('/csv')
def csv_skats():
    try:
        with open('dati.csv', mode='r', encoding="utf-8") as fails:
            csv_lasitajs = csv.reader(fails)
            dati = list(csv_lasitajs)
        return render_template('csv.html', dati=dati)
    except FileNotFoundError:
        with open('dati.csv', mode='w', encoding="utf-8", newline='') as fails:
            fails.write("Vārds,Uzvārds,Vecums\n")
        return render_template('kluda.html', zinojums="Fails dati.csv nav atrasts")

@app.route('/pievienot', methods=['POST'])
def pievienot():
    vards = request.form['vards']
    uzvards = request.form['uzvards']
    vecums = request.form['vecums']
    ierakstit_csv('dati.csv', [vards, uzvards, vecums])
    return redirect(url_for('csv_skats'))

def ierakstit_csv(faila_nosaukums, dati):
    fails_eksiste = os.path.isfile(faila_nosaukums)
    with open(faila_nosaukums, mode='a', encoding="utf-8", newline='') as fails:
        rakstitajs = csv.writer(fails)
        if not fails_eksiste:
            rakstitajs.writerow(['Vārds', 'Uzvārds', 'Vecums'])
        rakstitajs.writerow(dati)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Papildus datu demonstrācija
def izmeginajums():
    # CSV
    with open('dati.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        dati = [row for row in reader]
    print("CSV:", dati)

    # JSON
    with open('dati.json', 'r', encoding='utf-8') as file:
        dati_json = json.load(file)
    print("JSON:", dati_json)

    # XML
    with open('dati.xml', 'r', encoding='utf-8') as file:
        xml_string = file.read()
    data_dict = xmltodict.parse(xml_string)
    print("XML to JSON:", json.dumps(data_dict))

    # YAML
    with open('dati.yaml', 'r', encoding='utf-8') as file:
        dati_yaml = yaml.safe_load(file)
    print("YAML:", dati_yaml)

if __name__ == "__main__":
    # izmeginajums()  # Ja nepieciešams testēt
    app.run(debug=True)
