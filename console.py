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

owner1 = Owner("Bob and Laura Seaver", "11930893998", "homeward_bound@email.com", "343 Big Bear Road")
owner_repo.save(owner1)
owner2 = Owner("Alex Osbourne", "12345678940", "starburns@community.net", "5 Greendale Avenue")
owner_repo.save(owner2)
owner3 = Owner("John's Mum", "11234567890", "not-her-real-email@gmail.com", "394 Fake Street")
owner_repo.save(owner3)

animal1 = Animal("Sassy", "cat", "2008-04-30", owner1, vet1)
animal_repo.save(animal1)
animal2 = Animal("Shadow", "dog", "2013-08-08", owner1, vet1)
animal_repo.save(animal2)
animal3 = Animal("Chance", "dog", "2019-11-09", owner1, vet2)
animal_repo.save(animal3)
animal4 = Animal("Troy", "reptile", "2020-04-01", owner2, vet2)
animal_repo.save(animal4)

note1 = TreatmentNote("2022-02-25", "Six month health check, due flea and wormer and vaccines. BAR, really lovely indoor cat, in good shape for her age. Bit of tartar build-up on teeth but not bad enough to need a scale and polish yet. Recommend brushing a couple times a week if she tolerates it.", animal1)
note_repo.save(note1)
note2 = TreatmentNote("2022-04-21", "Sassy escaped from the house and went missing for a few days before being found yesterday in the woods by O's property, fur is matted but she tolerated us brushing her in consult. A bit shy compared to previous visit but ate some dreamies off the table in consult room. Otherwise seems perfectly healthy, no scratches or wounds anywhere, pain score of 0.", animal1)
note_repo.save(note2)