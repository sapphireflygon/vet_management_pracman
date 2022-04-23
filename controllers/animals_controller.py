from flask import Flask, Blueprint, render_template, request, redirect

from models.animal import Animal
import repositories.animal_repo as animal_repo

animals_blueprint = Blueprint("aminals", __name__)

