from flask import Flask, Blueprint, request, render_template, redirect

from models.owner import Owner
import repositories.owner_repo as owner_repo

owners_blueprint = Blueprint("owners", __name__)

