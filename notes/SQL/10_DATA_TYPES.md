# DATA TYPES

## GETTING FIELDS' DATA TYPES

 INFORMATION_SCHEMA.COLUMNS  
 INFORMATION_SCHEMA.TABLES  

```sql
SELECT column_name, data_type
FROM INFORMATION_SCHEMA.COLUMNS
WHERE column_name IN ('title', 'description', 'special_features') AND
                      table_name = 'film';
```

## DATE AND TIME

`TIMESTAMP` both time and date **yyyy-mm-dd hh:mm:ss**  
`DATE` only date  
`TIME` only time  

`INTERVAL` date and time as a period of time (years, months, days, hours, etc.)

## ARITHMETIC OPERATIONS ON DATE TIME

Intervals are usefull to do that

```sql
SELECT date + INTERVAL '3 days' as expected_return
FROM rental
```

will add 3 days to the `date` field and create a new column

## ARRAYS

Creating a table with arrays first

```sql
CREATE TABLE table_name (
  id int,
  field1 text[][],
  field2 int[],
)
```
Inserting data
```sql
INSERT INTO table_name (
  VALUES (1,
         '{{'work','work@gmail.com'},{'other,'other@mail.com'}',
         '{90, 98, 200}');
)
```

Selecting data
```sql
SELECT field1[2][1], field2[2][2], field3[1]
FROM table_name
```

```sql
SELECT field1[2][1], field2[2][2], field3[1]
FROM table_name
WHERE field[1][1] = {value}
```
`ANY` to match entries that have the value in any of its array data
```sql
SELECT field1[2][1], field2[2][2], field3[1]
FROM table_name
WHERE {value} = ANY (field1)
```

`@>` same as any, but different syntaxis
```sql
SELECT field1[2][1], field2[2][2], field3[1]
FROM table_name
WHERE field1 @> ARRAY[{value}]
```


## ARITMETIC WITH DAYS AND TIMES

Substract
```sql
SELECT DATE '2005-09-11' - '2005-09-10'
```
Returns 1 (int)

Add
```sql
SELECT DATE '2005-09-11' + INTEGER '3'
```
Returns a date

Substract timestamp
```sql
SELECT DATE '2005-09-11 00:00:00' - DATE '2005-09-09 12:00:00'
```
Returns an interval '1 day 12:00:00'

Adding to timestamp
```sql
SELECT TIMESTAPM '2005-09-11' + 21 * INTERVAL '1 day'
```

## AGE
Returs an inteval between 2 

## CURRENT DATE AND TIME

Get date and time with timezone
```sql
SELECT NOW()
```
Same as NOW()
```sql
SELECT CURRENT_TIMESTAMP
```
Round the seconds
```sql
SELECT CURRENT_TIMESTAMP(2)
```

Getting only datetime (casting)
```sql
SELECT NOW()::timestamp
```

Using cast
```sql
SELECT CAST(NOW() AS timestamp)
```

Also
``` CURRENT_DATE , CURRENT_TIME ```

## EXTRACT AND DATE_PART

```sql
EXTRACT({part} FROM {date_field})
DATE_PART('part', {date_field})
```
`quarter`, `year`, `month`, `day of week`, etc

## DATE_TRUNC

Truncates (sets to the start) the given date_part
```sql
DATE_TRUNC({part}, {date_field})
```
