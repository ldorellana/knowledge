
# MORE WINDOW FUNCTIONS

```sql
FUNC_NAME() OVER() AS {new_row_name}
```

## ROW NUMBER

```sql
ROW_NUMBER() OVER() AS row_N
```

### ORDER BY MULTIPLE COLUMNS

```sql
ROW_NUMBER() OVER({field1} DESC, {field2} ASC) AS {new_field}
``` 

## LAG
Returns the `{fields}'s` value **n** rows before the current row

```sql
LAG({field}, n) OVER() AS {new_field}
```

## PARTITION BY 
Splits the table into partititons from a column's unique values  
- Results arent rolled into one column like `GROUP BY`  
- `LAG` will only fetch within it spartition

```sql
LAG({filed1}, 1) OVER(PARTITION BY {field2}) AS {new_field}
```

Multiple partitions can be created like in `GROUP BY`
```sql
ROW_NUMBER({field1}, 1) OVER(PARTITION BY {field2}, {field3}) AS {new_field}
```
