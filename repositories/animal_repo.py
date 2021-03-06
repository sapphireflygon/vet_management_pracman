from db.run_sql import run_sql
from models.animal import Animal
import repositories.owner_repo as owner_repo
import repositories.vet_repo as vet_repo

# List all animals in database
def select_all():
    animals = []
    sql = "SELECT * FROM animals"
    results = run_sql(sql)
    for result in results:
        owner = owner_repo.select(result["owner_id"])
        if result["vet_id"] == None:
            animal = Animal(result["name"], result["species"], result["date_of_birth"], owner, "No vet", result["id"])
            animals.append(animal)
        else:
            vet = vet_repo.select(result["vet_id"])
            animal = Animal(result["name"], result["species"], result["date_of_birth"], owner, vet, result["id"])
            animals.append(animal)
    return animals

# Find one animal in database
def select(id):
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    owner = owner_repo.select(result["owner_id"])
    if result["vet_id"] == None:
        animal = Animal(result["name"], result["species"], result["date_of_birth"], owner,  "No vet", result["id"])
        print(animal.vet)
    else:
        vet = vet_repo.select(result["vet_id"])
        animal = Animal(result["name"], result["species"], result["date_of_birth"], owner, vet, result["id"])
    return animal

# Create new animal in database
def save(animal):
    sql = "INSERT INTO animals (name, species, date_of_birth, owner_id, vet_id) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [animal.name, animal.species, animal.date_of_birth, animal.owner.id, animal.vet.id]
    result = run_sql(sql, values)
    id = result[0]["id"]
    animal.id = id

# Delete all animals in database 
def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

# Delete one animal
def delete(id):
    sql = "DELETE FROM animals WHERE id=%s"
    values = [id]
    run_sql(sql, values)

# Update animal details
def update(animal):
    sql = "UPDATE animals SET (name, species, date_of_birth, owner_id, vet_id) = (%s, %s, %s, %s, %s) WHERE id=%s"
    values = [animal.name, animal.species, animal.date_of_birth, animal.owner.id, animal.vet.id, animal.id]
    run_sql(sql, values)
