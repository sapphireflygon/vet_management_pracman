from flask import Flask, Blueprint, render_template, request, redirect
\
from models.animal import Animal
from models.treatment_note import TreatmentNote
import repositories.animal_repo as animal_repo
import repositories.owner_repo as owner_repo
import repositories.vet_repo as vet_repo
import repositories.treatment_note_repo as note_repo

treatment_note_blueprint = Blueprint("treatment_note", __name__)

# Show one animal's treatment notes --> notes.html
@treatment_note_blueprint.route("/animals/<id>/notes")
def show_notes(id):
    animal = animal_repo.select(id)
    treatment_notes = note_repo.all_notes_for_one_animal(animal)
    return render_template("/treatment_notes/notes.html", animal=animal, treatment_notes=treatment_notes)

# Create new treatment note --> add_treatment_notes.html
@treatment_note_blueprint.route("/animals/<id>/notes/new")
def new_treatment_note(id):
    animal = animal_repo.select(id)
    return render_template("/treatment_notes/add_treatment_notes.html", animal=animal)

# Update animal's treatment notes with new note from form --> redirect back to notes.html
@treatment_note_blueprint.route("/animals/<id>/notes", methods=["POST"])
def update_treatment_notes(id):
    print(id)
    animal = animal_repo.select(id)
    date = request.form["date"]
    note = request.form["note"]
    new_note = TreatmentNote(date, note, animal)
    print(new_note)
    note_repo.save(new_note)
    return redirect(F"/animals/{id}/notes") # REALLY COOL THANK ELIN & JOHN FOR TEACHING ME ABOUT fstrings in routes/redirects!
