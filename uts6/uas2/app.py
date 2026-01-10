from flask import Flask, render_template, request, redirect
from utils import *

app = Flask(_name_)

# ================= MENU UTAMA =================
@app.route("/", methods=["GET", "POST"])
def menu():
    if request.method == "POST":
        p = request.form["pilihan"]

        # CEK BIODATA UNTUK MENU 2-5
        if p in ["2", "3", "4", "5"] and not biodata_lengkap():
            return redirect("/peringatan")
        
        if p == "1":
            return redirect("/biodata")
        elif p == "2":
            return redirect("/sks")
        elif p == "3":
            return redirect("/nilai")
        elif p == "4":
            return redirect("/lihat-nilai")
        elif p == "5":
            return redirect("/ip")

    return render_template("menu.html")


# ================= BIODATA (SUBMENU) =================
@app.route("/biodata", methods=["GET", "POST"])
def biodata_menu():
    if request.method == "POST":
        p = request.form["pilihan"]

        if p == "1":
            return redirect("/b