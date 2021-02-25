# Flask App

This is my flask app.

https://github.com/bradtraversy/myflaskapp

## Templating

http://flask.pocoo.org/docs/0.12/templating/

http://jinja.pocoo.org/docs/2.9/templates/

## Database Script

Lorem

### Create Database

```sql
CREATE DATABASE `FlaskBookStore`;
```

### User Table creation log

```sql
 CREATE TABLE `user` (id INT(11) UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT);
 ALTER TABLE `user` ADD `name` VARCHAR(50)  NOT NULL  DEFAULT ''  AFTER `id`;
 ALTER TABLE `user` ADD `username` VARCHAR(50)  NOT NULL  DEFAULT ''  AFTER `name`;
 ALTER TABLE `user` ADD `email` VARCHAR(50)  NOT NULL  DEFAULT ''  AFTER `username`;
 ALTER TABLE `user` ADD `password` VARCHAR(100)  NOT NULL  DEFAULT ''  AFTER `email`;
 ALTER TABLE `user` ADD `creation_date` DATE  NOT NULL  AFTER `password`;
 ALTER TABLE `user` ADD UNIQUE INDEX `username_unique` (`username`);
 ALTER TABLE `user` ADD UNIQUE INDEX `email_unique` (`email`);
```


### POSTS table create log 

```sql
 CREATE TABLE `posts` (id INT(11) UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT);
 ALTER TABLE `posts` ADD `title` VARCHAR(50)  NOT NULL  DEFAULT ''  AFTER `id`;
 ALTER TABLE `posts` ADD `body` TEXT  NULL  AFTER `title`;
 ALTER TABLE `posts` ADD `author` VARCHAR(20)  NOT NULL  DEFAULT ''  AFTER `body`;
 ALTER TABLE `posts` ADD `create_date` DATE  NOT NULL  AFTER `author`;
```

### Contacts table create log 
```sql

CREATE TABLE contacts (
    id INT(11) UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL DEFAULT '',
    company VARCHAR(50) NOT NULL DEFAULT '',
    email VARCHAR(50) NOT NULL DEFAULT '',
    note VARCHAR(500)
    )

```


## TODO 
 - Add Cookie base authentication (try to use JWT)
 - Implement Store Book.


