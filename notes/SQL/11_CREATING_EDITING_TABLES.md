# CREATING AND EDITING TABLES

## CREATE

```sql
CREATE TABLE IF NOT EXIST {table_name} (
  {field1} {data_type},
  {field2} {data_type}
);
```

## INSERTING

Just specific fields
```sql
INSERT INTO {table_name} (
  ({field1}, {field2}) VALUES ({value1}, {value2}));
```

All the fields in order
```sql
INSERT INTO {table_name} (
  VALUES ({value1}, {value2}));
```
