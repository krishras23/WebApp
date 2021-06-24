create database test;
use test;
create table  student (name varchar (20), age int );

rom trello.tasks where importance = 23

insert into test.student values ('krish', 16);
insert into test.student values ('joe', 17);

select * from test.student;

INSERT into tasks values ('buy groceries', 33, 'Krish');
INSERT into tasks values ('clearn room', 2, 'jones');


insert into the_tasks values (8.226, '2003-12-30', 3.67);
select * from the_tasks
DESCRIBE the_tasks insert into the_tasks values (8.226, '2003-12-30', 3.67);

use trello;
create table test_table (user_id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(40), password VARCHAR(255), email VARCHAR(255)))
INSERT into trello.test_table(username,password, email) values ("cow", "grass", "cows@cow.com");


ALTER TABLE tasks ADD created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

Drop table more_tasks

alter table trello.tasks
Drop importance;


ALTER TABLE trello.tasks
ADD COLUMN importance INT NOT NULL;

INSERT into trello.tasks (task_name,importance,owner) values ("does this work",9, "fluffy");

SELECT
    owner
FROM
    tasks
WHERE
    owner like "kapil";

UPDATE trello.tasks

SET
	owner = "Anvi"
WHERE
    owner like "kapil";




UPDATE trello.tasks

SET
	owner = "NotAnvi"
WHERE
    owner like "Anvi";

CREATE TABLE trello.events(
  id int auto_increment primary key,
  event_name varchar(255),
  visitor varchar(255),
  properties json,
  browser json


INSERT INTO trello.events(event_name, visitor,properties, browser)
VALUES (
  'pageview',
   '1',
   '{ "page": "/" }',
   '{ "name": "Safari", "os": "Mac", "resolution": { "x": 1920, "y": 1080 } }'
),
('pageview',
  '2',
  '{ "page": "/contact" }',
  '{ "name": "Firefox", "os": "Windows", "resolution": { "x": 2560, "y": 1600 } }'
),
(
  'pageview',
  '1',
  '{ "page": "/products" }',
  '{ "name": "Safari", "os": "Mac", "resolution": { "x": 1920, "y": 1080 } }'
),
(
  'purchase',
   '3',
  '{ "amount": 200 }',
  '{ "name": "Firefox", "os": "Windows", "resolution": { "x": 1600, "y": 900 } }'
),
(
  'purchase',
   '4',
  '{ "amount": 150 }',
  '{ "name": "Firefox", "os": "Windows", "resolution": { "x": 1280, "y": 800 } }'
),
(
  'purchase',
  '4',
  '{ "amount": 500 }',
  '{ "name": "Chrome", "os": "Windows", "resolution": { "x": 1680, "y": 1050 } }'
);

SELECT id, browser->'$.name' browser
FROM trello.events;

SELECT id, browser->'$.os' browser
FROM trello.events;


SELECT lastname, firstname, reportsTo, jobtitle
FROM employees
WHERE jobTitle = "Sales Rep"
AND reportsTo = 1143
ORDER BY lastName DESC;


SELECT DISTINCT
    state, city
FROM
    customers
WHERE
    state IS NOT NULL
ORDER BY
    state,
    city;



SELECT state, contactFirstName from customers where country like "USA" or country like "UK" and state NOT NULL order by state ;