class Animal:
    def __init__(self, id = None, input_species, input_name, input_date_of_birth, owner_id, vet_id, input_treatment_notes):
        self.id = id
        self.species = input_species
        self.name = input_name
        self.date_of_birth = input_date_of_birth
        self.owner_id = owner_id
        self.vet_id = vet_id
        self.treatment_notes = input_treatment_notes