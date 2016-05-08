CREATE TABLE models (
    model_id SERIAL PRIMARY KEY,
    year INTEGER NOT NULL,
    brand_name VARCHAR(50) NULL,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE brands (
    brand_id SERIAL PRIMARY KEY,
    brand_name VARCHAR(50) NOT NULL,
    founded INTEGER,
    headquarters VARCHAR(50),
    discontinued INTEGER
);

INSERT INTO brands (brand_name, founded, headquarters, discontinued)
VALUES ('Ford', 1903, 'Dearborn, MI', NULL),
('Chrysler', 1925, 'Auburn Hills, Michigan', NULL),
('Citroen', 1919, 'Saint-Ouen, France', NULL),
('Hillman', 1907, 'Ryton-on-Dunsmore, England', 1981),
('Chevrolet', 1911, 'Detroit, Michigan', NULL),
('Cadillac', 1902, 'New York City, NY', NULL),
('BMW', 1916, 'Munich, Bavaria, Germany', NULL),
('Austin', 1905, 'Longbridge, England', 1987),
('Fairthorpe', 1954, 'Chalfont St Peter, Buckinghamshire', 1976),
('Studebaker', 1852, 'South Bend, Indiana', 1967),
('Pontiac', 1926, 'Detroit, MI', 2010),
('Buick', 1903, 'Detroit, MI', NULL),
('Rambler', 1901, 'Kenosha, Washington', 1969),
('Plymouth', 1928, 'Auburn Hills, Michigan', 2001),
('Tesla', 2003, 'Palo Alto, CA', NULL);

INSERT INTO models (year, brand_name, name) VALUES
(1909, 'Ford', 'Model T'),
(1926, 'Chrysler', 'Imperial'),
(1948, 'Citroën', '2CV'),
(1950, 'Hillman', 'Minx Magnificent'),
(1953, 'Chevrolet', 'Corvette'),
(1954, 'Chevrolet', 'Corvette'),
(1954, 'Cadillac', 'Fleetwood'),
(1955, 'Chevrolet', 'Corvette'),
(1955, 'Ford', 'Thunderbird'),
(1956, 'Chevrolet', 'Corvette'),
(1957, 'Chevrolet', 'Corvette'),
(1957, 'BMW', '600'),
(1958, 'Chevrolet', 'Corvette'),
(1958, 'BMW', '600'),
(1958, 'Ford', 'Thunderbird'),
(1959, 'Austin', 'Mini'),
(1959, 'Chevrolet', 'Corvette'),
(1959, 'BMW', '600'),
(1960, 'Chevrolet', 'Corvair'),
(1960, 'Chevrolet', 'Corvette'),
(1960, 'Fillmore', 'Fillmore'),
(1960, 'Fairthorpe', 'Rockette'),
(1961, 'Austin', 'Mini Cooper'),
(1961, 'Studebaker', 'Avanti'),
(1961, 'Pontiac', 'Tempest'),
(1961, 'Chevrolet', 'Corvette'),
(1962, 'Pontiac', 'Grand Prix'),
(1962, 'Chevrolet', 'Corvette'),
(1962, 'Studebaker', 'Avanti'),
(1962, 'Buick', 'Special'),
(1963, 'Austin', 'Mini'),
(1963, 'Austin', 'Mini Cooper S'),
(1963, 'Rambler', 'Classic'),
(1963, 'Ford', 'E-Series'),
(1963, 'Studebaker', 'Avanti'),
(1963, 'Pontiac', 'Grand Prix'),
(1963, 'Chevrolet', 'Corvair 500'),
(1963, 'Chevrolet', 'Corvette'),
(1964, 'Chevrolet', 'Corvette'),
(1964, 'Ford', 'Mustang'),
(1964, 'Ford', 'Galaxie'),
(1964, 'Pontiac', 'GTO'),
(1964, 'Pontiac', 'LeMans'),
(1964, 'Pontiac', 'Bonneville'),
(1964, 'Pontiac', 'Grand Prix'),
(1964, 'Plymouth', 'Fury'),
(1964, 'Studebaker', 'Avanti'),
(1964, 'Austin', 'Mini Cooper');
