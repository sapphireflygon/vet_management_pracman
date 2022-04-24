class Animal:
    def __init__(self, input_name, input_species, input_date_of_birth, owner, vet, id=None):
        self.id = id
        self.species = input_species
        self.name = input_name
        self.date_of_birth = input_date_of_birth
        self.owner = owner
        self.vet = vet
        self.treatment_notes = {}