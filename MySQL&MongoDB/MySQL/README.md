```
$ mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.16 MySQL Community Server - GPL

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> CREATE DATABASE sample_db;
Query OK, 1 row affected (0.00 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sample_db          |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

mysql> CREATE TABLE table_example(
    -> first_name VARCHAR(20),
    -> last_name VARCHAR(20),
    -> gender CHAR(1),
    -> birthday DATE);
ERROR 1046 (3D000): No database selected
mysql> USE sample_db
Database changed
mysql> CREATE TABLE table_example( first_name VARCHAR(20), last_name VARCHAR(20), gender CHAR(1), birthday DATE);
Query OK, 0 rows affected (0.01 sec)

mysql> SELECT * FROM table_example
    -> ;
Empty set (0.00 sec)

mysql> INSERT INTO table_example(
    -> first_name, last_name, gender, birthday)
    -> VALUES(
    -> 'Mark','Smith','M','1990-01-01');
Query OK, 1 row affected (0.01 sec)

mysql> SELECT * FROM table_example;
+------------+-----------+--------+------------+
| first_name | last_name | gender | birthday   |
+------------+-----------+--------+------------+
| Mark       | Smith     | M      | 1990-01-01 |
+------------+-----------+--------+------------+
1 row in set (0.00 sec)

mysql> TRUNCATE TABLE table_example;
Query OK, 0 rows affected (0.01 sec)

mysql> SELECT * FROM table_example;
Empty set (0.01 sec)

mysql> TRUNCATE TABLE table_example;
Query OK, 0 rows affected (0.01 sec)

mysql> SELECT * FROM table_example;
Empty set (0.01 sec)

mysql> DROP DATABASE sample_db;
Query OK, 1 row affected (0.02 sec)

mysql> SHOW DATABESES;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'DATABESES' at line 1
mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)

```
