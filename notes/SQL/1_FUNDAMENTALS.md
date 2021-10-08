# NOTES


## COMMANDS

### SELECTING FIELDS

**SELECT**
```sql
SELECT {field} 
FROM {table};
```

**DISTINCT**
```sql
SELECT DISTINCT {field} 
FROM {table};
```

**COUNT** 
(counts not null if its a field)
```sql
SELECT COUNT(*) 
FROM {table};

```

***COUNT DISTINCT***
```sql
SELECT COUNT(DISTINCT {field}) 
FROM {table};

```

### FILTERING RESULTS

`=`   equal
`<>`  not equal
`<`   less
`>`   more
`<=`  less or equal
`>=`  more or equal

**WHERE**
```sql
SELECT {field} 
FROM {TABLE}
WHERE title = 'Metropolis';
```

***WHERE AND***
```sql
SELECT {field}
FROM {table}
WHERE {field} {condition} {value}
AND {field} {condition} {value};
```

***WHERE OR***
```sql
SELECT {field}
FROM {table}
WHERE {field} {condition} {value}
OR {field} {condition} {value};
```

**WHERE BETWEEN**
Between is inclusive, so both values are included
```sql
SELECT {field}
FROM {table}
WHERE {field} 
BETWEEN {value} AND {value};
```

***WHERE IN***
```sql
SELECT {fields}
FROM {table}
WHERE {field} IN (V1, ... V3);
```

***WHERE IS NULL***
```sql
SELECT {fields}
FROM {table}
WHERE {field} IS NULL;
```

***WHERE LIKE / NOT LIKE***
wildcards:
`%` matches zero, one or more characters
`_` mathces a single character

```sql
SELECT {fields}
FROM {table}
WHERE {field} LIKE/NOT LIKE {value with widlcard};
```

### AGGREGATE FUNCTIONS

- *AVG*
- *SUM*
- *MAX*
- *MIN*
- *COUNT*

```sql
SELECT {AGGF}(field)
FROM {table};
```
### ARITHMETIC FUNCTIONS

- `+ - * /`
- *ABS(n)*
- *CEIL(n) FLOOR()*
- *EXP(n)* elevate to e
- *LN(n)* (log nat)
- *MOD(n)*
- *POWER(n1, n2)* 
- *SQRT(N)*


*\ divison is normally integer results  
At least a number needs to have decimals
```sql
SELECT (4.0 / 3.0)
```

### ALIAS

**AS** 
*\ it can be omited and just leave a space
```sql
SELECT ({f1} {function} {f2}) [AS] {new_name}
FORM {table}
```

### ORDER BY
`DESC` to change the order
Multiple columns can be used 
```sql
SELECT {field} 
FROM {table}
ORDER BY {field, .. field} [DESC]
```

### GROUP BY
*\ always after the `FROM` clause
```sql
SELECT {field}, AGGF({field})
FROM {table}
GROUP BY {field}
```

### HAVING
WHERE can't use aggf, but HAVING can
```sql
SELECT {field}
FROM {table}
GROUP BY {field}
HAVING AGGF({field}) {condition} {value}
```









 
