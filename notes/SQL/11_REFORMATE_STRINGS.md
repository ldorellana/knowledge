# REFORMATING STRINGS

## CONCATENATE

`||` or `CONCAT('STR1', ' ', 'STR2')`

String and non-string data can be concatenated

## UPPER LOWER INITCAP

`UPPER(str)`, 'LOWER(str)', `INITCAP(STR)`

## REPLACE

```sql
SELECT 
  REPLACE(description, 'A Astounding', 'An Austounding') AS description
```

## REVERSE

```sql
SELECT title, REVERSE(title)
FROM film
```

## CHAR_LENGTH LENGTH

Return a string lenght

`CHAR_LENNGTH()`, `LENGTH()`

## POSITION AND STRPOS

```sql
POSITION('str' IN field)
STRPOS(field, 'str')
```

## LEFT / RIGHT 

```sql
RIGHT(field,)
```


