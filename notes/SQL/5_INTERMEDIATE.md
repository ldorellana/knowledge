# INTERMEDIATE SQL 

## CASE statement

composed of `WHEN`, `THEN`, `ELSE`, finished by `END`

```sql
CASE WHEN {field} {comparison} {value} THEN {value}
     WHEN {field} {comparison} {value} THEN {value}
     ELSE {value} 
     END
     AS {new_field}
```


```sql
SELECT {f1}, {f2},
  CASE WHEN {f1} {comparison} {f2} THEN {value}
       WHEN {f1} {comparison} {f2} THEN {value}
       ELSE {value} 
       END
       AS {new_field}
FROM {table}
WHERE {f3} {comparison} {value}
```

**here `WHERE` is really important to filter the `ELSE` results

### CASE in WHEN

`CASE` can also be used in the `WHEN` statement to filter as a column   
the only difference is that it does not include the alias

```sql
SELECT {f1}, {f2}
FROM {table}
WHERE (CASE WHEN {f1} {comparison} {f2} THEN {value}
       WHEN {f1} {comparison} {f2} THEN {value}
       ELSE {value} 
       END
       AS {new_field}) {comparison} {value}
```

### CASE with aggregate functions

Since aggregate functions require a column, the case statement can be used  

```sql
SELECT AGGFUN(CASE WHEN {f1} {comparison} {f2} 
                   THEN {value} END)
                   AS {new_field}
...
```
