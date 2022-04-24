from flask import Flask, Blueprint, render_template, redirect, request

from models.vet import Vet
import repositories.vet_repo as vet_repo

vets_blueprint = Blueprint("vets", __name__)

# vets.html
@vets_blueprint.route("/vets")
def vets():
    vets = vet_repo.select_all()
    return render_template("vets/vets.html", vets=vets)