from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hitung_volume", methods=["POST"])
def hitung_volume():
    sisi = float(request.form["sisi"])
    volume = sisi ** 3
    return render_template("index.html", hasil=volume)

if __name__ == "__main__":
    app.run(debug=True)
