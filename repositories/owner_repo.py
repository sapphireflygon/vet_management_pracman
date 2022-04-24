from db.run_sql import run_sql
from models.owner import Owner

# Create new owner in database
def save(owner):
    sql = "INSERT INTO owners (name, phone_number, email, address) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [owner.name, owner.phone_number, owner.email, owner.address]
    result = run_sql(sql, values)
    id = result[0]["id"]
    owner.id = id

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

