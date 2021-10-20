# PIVOTING

## CROSSTAB

`CREATE EXTENSION IF NOT EXIST tablefunc`

```sql
SELECT * FROM CROSSTAB($$
  source_sql TEXT
$$) AS ct ({field1} DATA_TYPE_1,
           {field2} DATA_TYPE_2,
           ...
           {fieldn} DATA_TYPE_N)
```

**FIELD NAMES MUST BE BETWEEN `""`**

## ROLLUP

Group level subtotals
Insted of doing totals and group totals as different queries  
and later doing UNION `ALL`

To generate group subtotals:
```sql
GROUP BY {field1}, ROLLUP({field2})
```
To generate group subtotals and general total:
```sql
GROUP BY ROLLUP({field1}, {field2})
```

## CUBE

Similar to `ROLLUP` but it's not hierarchical 
- Generates all possible group level aggregations

```sql
GROUP BY CUBE({field1}, {field2})
```
Unlike `ROLLUP`, `CUBE` generates subtotals for {field1}, {fiel2} and grand total


# COALESCE

Returns the first non-null value

`COALESCE(null, null, 1, null, 2) ? 1`

```sql
SELECT 
  COALESCE({field}, 'Default value')
  ...
```


# STRING_AGG

Takes all the values of a column and concatenates them

`STRING_AGG(column, separator)`

```sql
WITH {table1} as (...),

SELECT STRING_AGG({field}, ',')
FROM {table1}
```
