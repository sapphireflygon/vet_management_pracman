from flask import Flask, Blueprint, render_template, request, redirect

from models.animal import Animal
import repositories.animal_repo as animal_repo
import repositories.owner_repo as owner_repo
import repositories.vet_repo as vet_repo

animals_blueprint = Blueprint("animals", __name__)

# animals.html
@animals_blueprint.route("/animals")
def animals():
    animals = animal_repo.select_all()
    return render_template("animals/animals.html", animals=animals)