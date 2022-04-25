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

# new.htm
@animals_blueprint.route("/animals/new")
def new_animal():
    owners = owner_repo.select_all()
    vets = vet_repo.select_all()
    return render_template("/animals/new.html", owners=owners, vets=vets)

# after form for new animal, redirect to list of animals --> change to show page for animal??
@animals_blueprint.route("/animals", methods=["POST"])
def create_animal():
    name = request.form["name"]
    species = request.form["species"]
    date_of_birth = str(request.form["date_of_birth"])
    print(date_of_birth)
    owner_id = request.form["owner_id"]
    owner = owner_repo.select(owner_id)
    vet_id = request.form["vet_id"]
    vet = vet_repo.select(vet_id)
    new_animal = Animal(name, species, date_of_birth, owner, vet)
    animal_repo.save(new_animal)
    return redirect("/animals")

# Edit animal's details
@animals_blueprint.route("/animals/<id>/edit")
def edit_animal(id):
    animal = animal_repo.select(id)
    vets = vet_repo.select_all()
    owners = owner_repo.select_all()
    return render_template("/animals/edit.html", animal=animal, vets=vets, owners=owners)

# Update animal's details after editing
@animals_blueprint.route("/animals/<id>", methods=["POST"])
def update_animal(id):
    name = request.form["name"]
    species = request.form["species"]
    date_of_birth = str(request.form["date_of_birth"])
    print(date_of_birth)
    owner_id = request.form["owner_id"]
    owner = owner_repo.select(owner_id)
    vet_id = request.form["vet_id"]
    vet = vet_repo.select(vet_id)
    animal = Animal(name, species, date_of_birth, owner, vet, id)
    animal_repo.update(animal)
    return redirect("/animals")

# Delete animal from system
@animals_blueprint.route("/animals/<id>/delete", methods=["POST"])
def delete_animal(id):
    animal_repo.delete(id)
    return redirect("/animals")

# Show details of one animal --> show.html
@animals_blueprint.route("/animals/<id>")
def show_animal(id):
    animal = animal_repo.select(id)
    return render_template("/animals/show.html", animal=animal)

# Create new treatment note --> add_treatment_notes.html
@animals_blueprint.route("/animals/<id>/notes")
def new_treatment_note(id):
    animal = animal_repo.select(id)
    date = request.form["date_of_treatment"]
    treatment = request.form["treatment_note"]
    animal.treatment_notes = {str(date):treatment}
    # animal_repo.add_treatment(animal, date, treatment) # do we need this here??? 
    return render_template("/animals/add_treatment_notes.html", animal=animal, date=date, treatment=treatment)
    # might be getting lost between here and fx in animal_repo...
# Form has date input, and large text box to write treatment note; want to save these as dict key and value respectively; then update them to the animal.treatment_notes dictionary; then want to display each key:value pair in order (descending? so newest entry shows at top of treatment notes section of show page for animal); maybe have separate page to view all treatment notes if routes get funky???

# Update treatment notes on animal page --> redirect to
    # return redirect("/animals/<id>", animal=animal, date=date, treatment=treatment)
# Maybe need to create new page to view all treatments to avoid routes clashing??? ie weird if routing to /animals/<id> in multiple @blueprint functions????

