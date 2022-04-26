DROP TABLE IF EXISTS treatment_notes;
DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    phone_number VARCHAR(11), -- maybe figure out better data type for storage later if possible?
    email VARCHAR(255),
    address VARCHAR(255)
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255), 
    species VARCHAR(255),
    date_of_birth VARCHAR(10),
    owner_id INT NOT NULL REFERENCES owners(id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets(id) ON DELETE SET NULL -- don't delete on cascade, insteade ON DELETE SET NULL as can be null so if vet leaves business pets can be reassigned to a new vet if they're not leaving the practice too
);

CREATE TABLE treatment_notes (
    id SERIAL PRIMARY KEY,
    animal_id INT NOT NULL REFERENCES animals(id) ON DELETE CASCADE,
    date VARCHAR(10), 
    note TEXT
);