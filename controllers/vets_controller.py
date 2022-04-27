from flask import Flask, Blueprint, render_template, redirect, request

from models.vet import Vet
import repositories.vet_repo as vet_repo

vets_blueprint = Blueprint("vets", __name__)

# vets.html
@vets_blueprint.route("/vets")
def vets():
    vets = vet_repo.select_all()
    return render_template("vets/vets.html", vets=vets, title="Manage Vets")

# new.html
@vets_blueprint.route("/vets/new")
def new_vet():
    return render_template("vets/new.html", title="Create New Vet")

# after form for new vet, redirect to vets.html with new vets list
@vets_blueprint.route("/vets", methods=["POST"])
def create_vet():
    name = request.form["name"]
    new_vet = Vet(name)
    vet_repo.save(new_vet)
    return redirect("/vets")

# Edit vet's details
@vets_blueprint.route("/vets/<id>/edit")
def edit_vet(id):
    vet = vet_repo.select(id)
    return render_template("/vets/edit.html", vet=vet, title=f"Edit {vet.name}'s Details")

# Update vet's details after editing
@vets_blueprint.route("/vets/<id>", methods=["POST"])
def update_vet(id):
    name = request.form["name"]
    vet = Vet(name, id)
    vet_repo.update(vet)
    return redirect(f"/vets/{id}")

# Delete vet from system
@vets_blueprint.route("/vets/<id>/delete", methods=["POST"])
def delete_vet(id):
    vet_repo.delete(id)
    return redirect("/vets")

# Show details of one vet --> show.html
@vets_blueprint.route("/vets/<id>")
def show_vet(id):
    vet = vet_repo.select(id)
    assigned_animals = vet_repo.all_animals_assigned_to_vet(vet)
    return render_template("/vets/show.html", vet=vet, assigned_animals=assigned_animals, title=f"{vet.name}'s Details and Assigned Animals")