## WebApp

Install mysql packages
```
pip3 install mysql-connector-python
```

## TODO
- Find a sample database that has 20-30 tables, data, to run complex queries
- Order of [Execution](https://www.sisense.com/blog/sql-query-order-of-operations) 
- Make sure Update, Create with strings are working
- Python functions to write json as column 

## Git commands
- git status
- git diff
- git add <file-name> or git add . (all files)
- git diff --cached 
- git commit -m "message"
- git push origin main

## SQL Joins
- (INNER) JOIN: Returns records that have matching values in both tables
- LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
- RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
- FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table

## MySQL Server

- docker run --name=sqlserver -p 3306:3306 -e MYSQL_ROOT_PASSWORD=tomato -d mysql