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

# COMPLES SUBQUERIES

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
