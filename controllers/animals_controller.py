from flask import Flask, Blueprint, render_template, request, redirect
from datetime import datetime

from models.animal import Animal
import repositories.animal_repo as animal_repo
import repositories.owner_repo as owner_repo
import repositories.vet_repo as vet_repo

animals_blueprint = Blueprint("animals", __name__)

# animals.html
@animals_blueprint.route("/animals")
def animals():
    animals = animal_repo.select_all()
    no_vet = None
    return render_template("animals/animals.html", animals=animals, no_vet = no_vet, title="Manage Animals")

# new.html
@animals_blueprint.route("/animals/new")
def new_animal():
    owners = owner_repo.select_all()
    vets = vet_repo.select_all()
    current_date = datetime.now()
    return render_template("/animals/new.html", owners=owners, vets=vets, current_date=current_date, title="Create New Animal")

# After form to create a new animal, redirect to that animal's details page
@animals_blueprint.route("/animals", methods=["POST"])
def create_animal():
    name = request.form["name"]
    species = request.form["species"]
    date_of_birth = str(request.form["date_of_birth"])
    owner_id = request.form["owner_id"]
    owner = owner_repo.select(owner_id)
    vet_id = request.form["vet_id"]
    vet = vet_repo.select(vet_id)
    new_animal = Animal(name, species, date_of_birth, owner, vet)
    animal_repo.save(new_animal)
    return redirect(f"/animals/{new_animal.id}")

# Edit animal's details --> edit.html
@animals_blueprint.route("/animals/<id>/edit")
def edit_animal(id):
    animal = animal_repo.select(id)
    vets = vet_repo.select_all()
    owners = owner_repo.select_all()
    current_date = datetime.now()
    return render_template("/animals/edit.html", animal=animal, vets=vets, owners=owners, current_date=current_date, title=f"Edit {animal.name}'s Details")

# Update animal's details after editing
@animals_blueprint.route("/animals/<id>", methods=["POST"])
def update_animal(id):
    name = request.form["name"]
    species = request.form["species"]
    date_of_birth = str(request.form["date_of_birth"])
    owner_id = request.form["owner_id"]
    owner = owner_repo.select(owner_id)
    vet_id = request.form["vet_id"]
    vet = vet_repo.select(vet_id)
    animal = Animal(name, species, date_of_birth, owner, vet, id)
    animal_repo.update(animal)
    return redirect(f"/animals/{id}")

# Delete animal from system
@animals_blueprint.route("/animals/<id>/delete", methods=["POST"])
def delete_animal(id):
    animal_repo.delete(id)
    return redirect("/animals")

# Show details of one animal --> show.html
@animals_blueprint.route("/animals/<id>")
def show_animal(id):
    animal = animal_repo.select(id)
    no_vet = None
    return render_template("/animals/show.html", animal=animal, no_vet=no_vet, title=f"{animal.name}'s Details")

