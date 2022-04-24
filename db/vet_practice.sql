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
    phone_number INT NOT NULL,
    email VARCHAR(255),
    address VARCHAR(255)
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255), 
    species VARCHAR(255),
    date_of_birth VARCHAR(255),
    owner_id INT NOT NULL REFERENCES owners(id) ON DELETE CASCADE,
    vet_id INT NOT NULL REFERENCES vets(id) ON DELETE CASCADE,
    treatment_notes TEXT
);