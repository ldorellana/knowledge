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
