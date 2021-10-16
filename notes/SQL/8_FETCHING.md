# FETCHING

## RELATIVE

- `LAG({field}, n)` fetches a field's value at n rows before the current row
- `LEAD({field}, n)` fetches a field's value at n rows after the current row

## ABSOLUTE

- `FIRST_VALUE({field})` returns the first value of a table or partition
- `LAST_VALUE({field})` returns the last vlaue of a table or partitition
   
   
**A WINDOW BY DEFAULT STARTS AT THE BEGINNING OR A TABLE OR PARTITION  
AND ENDS AT THE CURRENT ROW**

So to allow `LAST_VALUE` to go from the end to beginning and not from current row  
`RANGE BETWEEN UNBOUNDED PRECEDING  AND UNBOUNDED FOLLOWING` is needed

```sql
LAST_VALUE({field}) OVER(ORDER BY year 
                         RANGE BETWEEN UNBOUNDED PRECIDING AND
                                       UNBOUNDED FOLLOWING
) AS last_value
```

## RANKING

- `ROW_NUMBER({field})` always assigns unique number, even if they have the same value
- `RANK({field})` assigns the same number if identical values, skips the next in that case
- `DENSE_RANK({})` assigns the same number if identical, but does not skip the next value

## PAGING

Divide data en approximately equl chunks

- Many API's return data in pages to reduce the data size sent
- Separate data into quartiles to judge performance

`NTILE(n)` splits the data into **n** pages

Creates a new column with the page number of each row
