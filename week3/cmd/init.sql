CREATE TABLE employee(
    emp_id char(6) UNIQUE NOT NULL,
    gender varchar(6) NOT NULL,
    name varchar(20) NOT NULL,
    address varchar(100),
    department smallint,
    manager char(6),
    age smallint NOT NULL,
    position varchar(30)
);

INSERT INTO employee 
values
    ('A00001', 'Male', 'Moon', '10-199, Gang-nam, Seoul', 1, 'C00001', 30, 'Senior engineer'),
    ('B00100', 'Female', 'Sun', '587/8, Gwan-ak, Seoul', 2, 'B00102', 25, 'Associate marketer'),
    ('A08771', 'Others', 'Peach', '203-3, Guro, Seoul', 1, 'C00001', 26, 'Junior engineer'),
    ('C00129', 'Male', 'Alex', '20-331, Bundang, Gyonggi', 3, 'C00002', 40, 'Director'),
    ('C00001', 'Male', 'Lion', '53-3, Namyang-ju, Gyonghi', 1, 'C00000', 55, 'CTO'),
    ('C00002', 'Others', 'Cindy', '100, Jong-ro, Seoul', 3, 'C00000', 52, 'Director'),
    ('B00102', 'Female', 'Ran', '290-10, Gwanghwamun, Seoul', 2, 'C00000', 45, 'Director'),
    ('C00000', 'Male', 'K', '1010, Sung-soo, Seoul', NULL, NULL, 51, 'CEO');

CREATE TABLE visit_log(
    visitor char(6),
    enter TIMESTAMP NOT NULL,
    out TIMESTAMP,
    purpose varchar(50)
);

INSERT INTO visit_log
values
    ('A00001', '2022-07-11 11:00:00', '2022-07-11 18:00:00','work'),
    ('B00100', '2022-07-11 10:00:00', '2022-07-11 19:00:00', 'work'),
    ('A08771', '2022-07-11 09:00:00', '2022-07-11 17:56:00', 'work'),
    ('C00129', '2022-07-11 09:00:00', '2022-07-11 18:20:00', 'work'),
    (NULL, '2022-07-11 12:30:00', '2022-07-11 14:45:00', 'meeting'),
    ('C00001', '2022-07-11 09:20:00', '2022-07-11 18:00:00', 'work'),
    ('C00002', '2022-07-11 09:30:00', '2022-07-11 18:20:00', 'work'),
    ('A00001', '2022-07-12 08:15:00', '2022-07-12 17:56:00', 'work'),
    ('B00100', '2022-07-12 08:30:00', '2022-07-12 19:00:00', 'work'),
    ('A08771', '2022-07-12 09:20:00', '2022-07-12 18:20:00', 'work'),
    (NULL, '2022-07-12 15:20:00', '2022-07-12 16:50:00', 'visit family'),
    ('C00129', '2022-07-12 10:00:00', '2022-07-12 18:00:00', 'work'),
    ('C00001', '2022-07-12 10:00:00', '2022-07-12 18:00:00', 'work'),
    ('C00002', '2022-07-12 09:00:00', '2022-07-12 17:56:00', 'work'),
    ('A00001', '2022-07-13 09:00:00', '2022-07-13 18:20:00', 'work'),
    ('B00100', '2022-07-13 08:30:00', '2022-07-13 18:00:00', 'work'),
    ('A08771', '2022-07-13 09:20:00', '2022-07-13 18:00:00', 'work'),
    ('C00129', '2022-07-13 10:00:00', '2022-07-13 18:00:00', 'work'),
    ('C00001', '2022-07-13 09:20:00', '2022-07-13 18:20:00', 'work'),
    ('C00002', '2022-07-13 08:15:00', '2022-07-13 17:56:00', 'work'),
    ('A00001', '2022-07-14 08:30:00', NULL, 'work'),
    ('B00100', '2022-07-14 08:30:00', NULL, 'work'),
    ('A08771', '2022-07-14 08:30:00', NULL, 'work');
    