# WINDOW FUNCTIONS

Perform calcularions on an already generated result set (a window)
- Perform aggregations without grouping
- Similar to subqueries in `SELECT`
- Used to calculate Running totals, rankings, moving averages

## OVER()
With subquery:

```sql
SELECT {field}, 
       {field}, (
  SELECT AGGF({field})
  FROM {table}
) AS {new_name}
FROM {table}
```

With WINDOW FUNCTION
```sql
SELECT {field1}, 
       {field2},
       AGGF({field}) **OVER()** AS {new_name}
```

## RANK() OVER()

```sql
SELECT {field}, 
       {field},  
       RANK() OVER(ORDER BY {field} AS {new_name}
FROM {table}
```

**Window functions are processed after the entire query except the final `ORDER BY`**
The functions uses the result set to calcualte info, not the DB
**Available in PostgreSQL, ORACLE, MySQL, SQL Server...
... NOT SQLite

## OVER and PARTITION BY

- Calculate separete values for different categories
- Calculate different calculations in the same column

```sql
AGGF({field1}) OVER(PARTITION BY {field2})
```
