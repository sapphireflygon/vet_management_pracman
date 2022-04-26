from db.run_sql import run_sql
from models.animal import Animal
from models.treatment_note import TreatmentNote
import repositories.treatment_note_repo as note_repo
import repositories.animal_repo as animal_repo

# List all notes for a pet
def all_notes_for_one_animal(animal):
    notes = []
    sql = "SELECT treatment_notes.* FROM treatment_notes INNER JOIN animals ON treatment_notes.animal_id = animals.id WHERE animals.id=%s"
    values = [animal.id]
    results = run_sql(sql, values)
    for result in results:
        note = TreatmentNote(result["date"], result["note"], animal)
        notes.append(note)
    return reversed(notes)

# Save new treatment note to the database
def save(treatment_note):
    sql = "INSERT INTO treatment_notes (date, note, animal_id) VALUES (%s, %s, %s) RETURNING id"
    values = [treatment_note.date, treatment_note.note, treatment_note.animal.id]
    result = run_sql(sql, values)
    id = result[0]["id"]
    treatment_note.id = id