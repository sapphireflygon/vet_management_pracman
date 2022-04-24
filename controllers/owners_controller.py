from flask import Flask, Blueprint, request, render_template, redirect

from models.owner import Owner
import repositories.owner_repo as owner_repo

owners_blueprint = Blueprint("owners", __name__)

# owners.html
@owners_blueprint.route("/owners")
def owners():
    owners = owner_repo.select_all()
    return render_template("owners/owners.html", owners=owners)