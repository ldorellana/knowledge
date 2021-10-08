# SET THEORY CLAUSES


## UNION
a set that puts the two tables together   
keepin all the entries but without duplicates  
like a set() in python

## UNION ALL
like concatenating 2 list together in python   
Keeps all the entries even duplicates

## INTERSECT
Includes only the records in both of the tables

## EXECPT
Includes the records only in one table

## SEMI-JOIN SUB-QUERY
Using the right table to see what records to keep on the left  
Like the `WHERE` clause  

```sql
SELECT {field1}, {fiels2}
FROM {table1}
WHERE {field1} IN
     (SELECT {field}
      FROM {table2}
      WHERE {field} {condition} {value})
```

## ANTI-JOIN SUB-QUERY
Using the right table to see what records to keep on the left  
Like the `WHERE` clause  

```sql
SELECT {field1}, {fiels2}
FROM {table1}
WHERE {field1} **NOT** IN
     (SELECT {field}
      FROM {table2}
      WHERE {field} {condition} {value})
```
