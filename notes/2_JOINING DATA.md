# JOINING DATA

## INNER JOIN
only get entries in both tables
```sql
SELECT {t1.field}, {t1.field}, {filed}
FROM {table1} AS t1
  INNER JOIN {table2} AS t2
    ON t1.x = t2.x
```
## LEFT / RIGHT JOIN
Unlike inner, it keeps all the entries in the   
right or left.

## FULL JOIN
Keeps all the entries  of both tables

## USING
if both tables have the same name for the   
joining field
```sql
SELECT * 
FROM table1
  INNER JOIN table2
    USING ({field})
```

## SELF-ISH JOINS
join the table with itself   
Can  be useful when se want to obtain join two    
fields from the same table with another in common.
|country|contintent|language|
if we join with itself in continent, we would get   
all the combinations of countries in that continent
*including the same countries*
```sql
SELECT {t1.field}, {t2.field}
FROM table AS t1
  INNER JOIN table AS t2
    ON t1.field = t2.field
LIMIT 15
```
To prevent the same country appering on the self join
```sql
SELECT {t1.field}, {t2.field}
FROM table AS t1
  INNER JOIN table AS t2
    ON t1.field = t2.field AND t1.field2 <> t2.field2
LIMIT 15
```

## CROSS JOIN
Makes a combination of all the values in the two tables
