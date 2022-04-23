from flask import Flask, Blueprint, render_template, redirect, request

from models.vet import Vet
import repositories.vet_repo as vet_repo

vets_blueprint = Blueprint("vets", __name__)

