# SUBQUERIES

## WHERE
AS A CONDITION
```sql
SELECT * 
FROM {table1}
WHERE {field} IN (SELECT {field}
                  FROM {table2}
                  WHERE {field} = {value}
)
```

## SELECT
AS A FIELD
```sql
SELECT {field}, (SELECT AGGF({field})
                 FROM {table2}
                 WHERE table1.{field} = table2.field()
) AS {field name}
FROM {table1}
```


## FROM
AS A TEMPORARY TABLE
```sql
SELECT {table1.field}, {subtable2.field}
FROM {table1}, (SELECT {field}, AGGF({field})
                FROM {table2}
                GROUP BY {field}
                ) AS subtable2
...
```

# SIMPLE SUBQUERIES

`WHERE`
- The subqueries are only evaluated once
- Can only return a single column

`FROM`
- Can return more than one column
- Can create multiple subqueries in one `FROM` statement
  - Alias them
  - Join them (include joining columns fro both)
- Can join a subquery with a table in  `FROM`
  - Include joinin columns for both

`SELECT`
- Must return a single value
- Filter both query and subquery correctly

# BEST PRACTICES

- FORMAT QUERIES
  - `SELECT`, `FROM`, `WHERE` and `GROUP BY` with correct order
  - Annotate the queries /* Query explanation */ or -- inline comment
  - Properly indent
  - Make sure all the filters are right in each subquery and the main 


# CORRELATED SUBQUERY

- Uses values from the outer query to generate a result
- Re-run for every row generated in the final data set
- Used for: advanced joinin, filtering and evaluating data

# COMMON TABLE EXPRESSIONS CTEs

Table declared before the main query

- CTEs are stores in memory
- Improves performance
- Improves organization
- Reference other CTEs (in order)  
- Reference itself *recursive CTE* (SELF JOIN)

```sql
WITH 

{table1} AS (
  SELECT {field}, {field}
  FROM {table1}
  ),

{table2} AS (
  SELECT {field}, {field}
  FROM {table1}
)
  
)

SELECT AGGF({field}) AS {new_name}
FROM cte;

```
