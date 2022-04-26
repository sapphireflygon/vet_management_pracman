import pdb

from models.animal import Animal
import repositories.animal_repo as animal_repo

from models.owner import Owner
import repositories.owner_repo as owner_repo

from models.vet import Vet
import repositories.vet_repo as vet_repo

from models.treatment_note import TreatmentNote
import repositories.treatment_note_repo as note_repo

animal_repo.delete_all()
owner_repo.delete_all()
vet_repo.delete_all()

vet1 = Vet("Hershel Green")
vet_repo.save(vet1)
vet2 = Vet("John Doolittle")
vet_repo.save(vet2)
vet3 = Vet("Test Delete")
vet_repo.save(vet3)

owner1 = Owner("Bob and Laura Seaver", "119308939", "homeward_bound@email.com", "343 Big Bear Road")
owner_repo.save(owner1)
owner2 = Owner("Alex Osbourne", "123456777", "starburns@community.net", "5 Greendale Avenue")
owner_repo.save(owner2)

animal1 = Animal("Sassy", "cat", "2008-04-30", owner1, vet1)
animal_repo.save(animal1)
animal2 = Animal("Shadow", "dog", "2013-08-08", owner1, vet1)
animal_repo.save(animal2)
animal3 = Animal("Chance", "dog", "2019-11-09", owner1, vet2)
animal_repo.save(animal3)
animal4 = Animal("Abed", "reptile", "2020-04-01", owner2, vet2)
animal_repo.save(animal4)

note1 = TreatmentNote("2022-04-25", "Note goes here woop", animal1)
note_repo.save(note1)

# animal_repo.delete(animal2.id)
# owner_repo.delete(owner2.id)
# vet_repo.delete(vet3.id)

# vet_repo.select_all()
# animal_repo.select_all()
# owner_repo.select_all()

# vet_repo.select(vet1.id)
# owner_repo.select(owner2.id)
# animal_repo.select(animal3.id)

# pdb.set_trace()