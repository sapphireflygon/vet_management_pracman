from db.run_sql import run_sql
from models.animal import Animal
import repositories.animal_repo as animal_repo
import repositories.owner_repo as owner_repo
import repositories.vet_repo as vet_repo

# List all animals in database
def select_all():
    animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)
    for result in results:
        owner = owner_repo.select(result["owner_id"])
        vet = vet_repo.select(result["vet_id"])
        animal = Animal(result["id"], result["species"], result["name"], result["date_of_birth"], owner, vet, result["treatment_notes"])
        animals.append(animal)
    return animals

# Find one animal in database
def select(id):
    sql = "SELECT * FROM animals WHERE id = %s"
    values = ["id"]
    result = run_sql(sql, values)
    owner = owner_repo.select(result["owner_id"])
    vet = vet_repo.select(result["vet_id"])
    animal = Animal(result["id"], result["species"], result["name"], result["date_of_birth"], owner, vet, result["treatment_notes"])
    return animal
