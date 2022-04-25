from flask import Flask, Blueprint, render_template, redirect, request

from models.vet import Vet
import repositories.vet_repo as vet_repo

vets_blueprint = Blueprint("vets", __name__)

# vets.html
@vets_blueprint.route("/vets")
def vets():
    vets = vet_repo.select_all()
    return render_template("vets/vets.html", vets=vets)

# new.html
@vets_blueprint.route("/vets/new")
def new_vet():
    return render_template("vets/new.html")

# after form for new vet, redirect to vets.html with new vets list
@vets_blueprint.route("/vets", methods=["POST"])
def create_vet():
    name = request.form["name"]
    new_vet = Vet(name)
    vet_repo.save(new_vet)
    return redirect("/vets")


