from flask import Flask, render_template, request, redirect
from utils.google_sheet import get_dua_counts, add_dua_entry

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        dua = request.form.get("dua")
        count = int(request.form.get("count", 0))

        if name and dua and count > 0:
            add_dua_entry(name, dua, count)
            return redirect("/")

    all_duas = get_dua_counts()
    return render_template("index.html", duas=all_duas)

if __name__ == "__main__":
    app.run(debug=True)
