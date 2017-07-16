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
/* 18:44:30 127.0.0.1 FlaskBookStore */ CREATE TABLE `user` (id INT(11) UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT);

/* 18:46:50 127.0.0.1 FlaskBookStore */ ALTER TABLE `user` ADD `username` VARCHAR(50)  NOT NULL  DEFAULT ''  AFTER `id`;

/* 18:47:29 127.0.0.1 FlaskBookStore */ ALTER TABLE `user` ADD `email` VARCHAR(50)  NOT NULL  DEFAULT ''  AFTER `username`;

/* 18:48:10 127.0.0.1 FlaskBookStore */ ALTER TABLE `user` ADD `password` VARCHAR(100)  NOT NULL  DEFAULT ''  AFTER `email`;

/* 18:48:37 127.0.0.1 FlaskBookStore */ ALTER TABLE `user` ADD `creation_date` DATE  NOT NULL  AFTER `password`;

/* 18:49:56 127.0.0.1 FlaskBookStore */ ALTER TABLE `user` ADD UNIQUE INDEX `username_unique` (`username`);


/* 18:50:40 127.0.0.1 FlaskBookStore */ ALTER TABLE `user` ADD UNIQUE INDEX `email_unique` (`email`);

```


### POSTS table create log 

```sql
/* 20:38:36 127.0.0.1 FlaskBookStore */ CREATE TABLE `posts` (id INT(11) UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT);

/* 20:39:51 127.0.0.1 FlaskBookStore */ ALTER TABLE `posts` ADD `title` VARCHAR(50)  NOT NULL  DEFAULT ''  AFTER `id`;

/* 20:40:12 127.0.0.1 FlaskBookStore */ ALTER TABLE `posts` ADD `body` TEXT  NULL  AFTER `title`;

/* 20:41:03 127.0.0.1 FlaskBookStore */ ALTER TABLE `posts` ADD `author` VARCHAR(20)  NOT NULL  DEFAULT ''  AFTER `body`;

/* 20:41:29 127.0.0.1 FlaskBookStore */ ALTER TABLE `posts` ADD `create_date` DATE  NOT NULL  AFTER `author`;
```