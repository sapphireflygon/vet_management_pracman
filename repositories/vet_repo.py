from db.run_sql import run_sql
from models.vet import Vet
from models.animal import Animal
import repositories.owner_repo as owner_repo

# List all vets in database
def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for result in results:
        vet = Vet(result["name"], result["id"])
        vets.append(vet)
    return vets

# Find one vet in database
def select(id):
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    vet = Vet(result["name"], result["id"])
    return vet

# Create new vet in database
def save(vet):
    sql = "INSERT INTO vets (name) VALUES (%s) RETURNING id"
    values = [vet.name]
    result = run_sql(sql, values)
    id = result[0]["id"]
    vet.id = id

# Delete all vets in database
def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

# Delete one vet
def delete(id):
    sql = "DELETE FROM vets WHERE id=%s"
    values = [id]
    run_sql(sql, values)

# Update vet details
def update(vet):
    sql = "UPDATE vets SET name = %s WHERE id = %s"
    values = [vet.name, vet.id]
    run_sql(sql, values)

# List of all pets assigned to specific vet:
def all_animals_assigned_to_vet(vet):
    animals = []
    sql = "SELECT animals.* FROM animals INNER JOIN vets ON animals.vet_id = vets.id WHERE vets.id = %s"
    values = [vet.id]
    results = run_sql(sql, values)

    for result in results:
        owner = owner_repo.select(result["owner_id"])
        animal = Animal(result["name"], result["species"], result["date_of_birth"], owner, vet, result["id"])
        animals.append(animal)
    return animals