from flask import Flask, Blueprint, request, render_template, redirect

from models.owner import Owner
import repositories.owner_repo as owner_repo

owners_blueprint = Blueprint("owners", __name__)

# owners.html
@owners_blueprint.route("/owners")
def owners():
    owners = owner_repo.select_all()
    return render_template("owners/owners.html", owners=owners)

# new.html
@owners_blueprint.route("/owners/new")
def new_owner():
    return render_template("owners/new.html")

# after form for new owner, redirect to owners.html with new owner added to list
@owners_blueprint.route("/owners", methods=["POST"])
def create_owner():
    name = request.form["name"]
    phone_number = request.form["phone_number"]
    email = request.form["email"]
    address = request.form["address"]
    new_owner = Owner(name, phone_number, email, address)
    owner_repo.save(new_owner)
    return redirect("/owners")