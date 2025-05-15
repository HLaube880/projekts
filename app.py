from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about_us')
def about_us():
    return render_template("about_us.html")

@app.route('/anketa')
def anketa():
    return render_template("anketa.html")

@app.route('/basics_syntax')
def basics_syntax():
    return render_template("basics_syntax.html")

@app.route('/independent2')
def independent2():
    return render_template("independent2.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/survey')
def survey():
    return render_template("survey.html")

@app.route('/sveiciens')
def sveiciens():
    return render_template("sveiciens.html")

@app.route('/mainigie')
def mainigie():
    vards = "Igors"
    vecums = 35
    skaitlis1 = 6
    skaitlis2 = 7
    summa = skaitlis1 + skaitlis2
    return render_template("mainigie.html", vards=vards, vecums=vecums, summa=summa)

@app.route('/operatori')
def operatori():
    return render_template("operatori.html")

@app.route('/kontroles_strukturas')
def kontroles_strukturas():
    return render_template("kontroles_strukturas.html")

@app.route('/funkcijas')
def funkcijas():
    return render_template("funkcijas.html")

@app.route('/ievade_izvade')
def ievade_izvade():
    return render_template("ievade_izvade.html")

@app.route('/failu_apstrade')
def failu_apstrade():
    return render_template("failu_apstrade.html")

@app.route('/oop')
def oop():
    return ("oop.html")

@app.route('/joks')
def joks():
    return render_template("joks.html")

@app.route('/csv2')
def csv2():
    return render_template("csv2.html")
  
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
