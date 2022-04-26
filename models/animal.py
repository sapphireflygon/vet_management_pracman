class Animal:
    def __init__(self, input_name, input_species, input_date_of_birth, owner, vet=None, id=None):
        self.id = id
        self.name = input_name
        self.species = input_species
        self.date_of_birth = input_date_of_birth
        self.owner = owner
        self.vet = vet