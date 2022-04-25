from db.run_sql import run_sql
from models.owner import Owner
from models.animal import Animal
import repositories.vet_repo as vet_repo

# Create new owner in database
def save(owner):
    sql = "INSERT INTO owners (name, phone_number, email, address) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [owner.name, owner.phone_number, owner.email, owner.address]
    result = run_sql(sql, values)
    id = result[0]["id"]
    owner.id = id

# List all owners in database
def select_all():
    owners = []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for result in results:
        owner = Owner(result["name"], result["phone_number"], result["email"], result["address"], result["id"])
        owners.append(owner)
    return owners

# Find owner in database
def select(id):
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    owner = Owner(result["name"], result["phone_number"], result["email"], result["address"], result["id"])
    return owner

# Delete all owners from database
def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

# Delete one owner
def delete(id):
    sql = "DELETE FROM owners WHERE id=%s"
    values = [id]
    run_sql(sql, values)

# Update owner details
def update(owner):
    sql = "UPDATE owners SET (name, email, phone_number, address) = (%s, %s, %s, %s) WHERE id=%s"
    values = [owner.name, owner.email, owner.phone_number, owner.address, owner.id]
    run_sql(sql, values)

# List of all pets owned by specific owner
def all_animals_owned_by_owner(owner):
    animals = []
    sql = "SELECT animals.* FROM animals INNER JOIN owners ON animals.owner_id = owners.id WHERE owners.id = %s"
    values = [owner.id]
    results = run_sql(sql, values)

    for result in results:
        vet = vet_repo.select(result["vet_id"])
        animal = Animal(result["name"], result["species"], result["date_of_birth"], owner, vet, result["id"])
        animals.append(animal)
    return animals