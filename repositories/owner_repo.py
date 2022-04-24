from db.run_sql import run_sql
from models.owner import Owner

# Create new owner in database
def save(owner):
    sql = "INSERT INTO owners (name, phone_number, email, address) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [owner.name, owner.phone_number, owner.email, owner.address]
    result = run_sql(sql, values)
    owner.id = result[0]["id"]
    return owner

