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
- Partition can have one or more columns (like pandas' groupby)
- Partition can work with different aggf
```sql
AGGF({field1}) OVER(PARTITION BY {field2})
```
# SLIDING WINDOWS

- Calculation relative to the current row
- running totals, sums, averages, etc
  
**ROWS VS RANGE BETWEEN**
RANGE takes together ROWS that have the same value
ROWS IS USED MOST OF THE TIME

```sql
ROWS BETWEEN <start> AND <finish>
```
```sql
RANGE BETWEEN <start> AND <finish>
```
```sql
PRECEDING -- no of rows before 
FOLLOWING -- no of rows after
UNBOUNDED PRECEDING -- every row since the beginning
UNBOUNDED FOLLOWING -- every row since the end
CURRENT ROW -- stop at current row
```

EXAMPLE
**RUNNING TOTAL**
```sql
SELECT 
       date,
       home_goal,
       away_goal,
       SUM(home_goal + away_goal) 
              OVER(ORDER BY date ROWS BETWEEN
                   UNBOUNDED PRECEDING AND CURRENT ROW)
           AS runnint_total
FROM match
WHERE hometeam_id = xx AND season = xxx
```

**CURRENT AND PREVIOUS**
```sql
SELECT 
       date,
       home_goal,
       away_goal,
       SUM(home_goal + away_goal) 
              OVER(ORDER BY date ROWS BETWEEN
                   1 PRECEDING AND CURRENT ROW)
           AS last2
FROM match
WHERE hometeam_id = xx AND season = xxx
```


`FIRST_ROW`, `LAST_ROW`, `MAX`, `MIN`, `SUM`, `AVG` 
