# ClanCoin
ClanCoin is a payment web application for organizations. Examples of use include sending currency from parents to their children as household spending money, and from children to their parents for game time and outings.
<br/>

<p align="center">
  <img src="https://user-images.githubusercontent.com/78391723/236469298-9c3a11c1-ebe9-4e48-bc79-3192bdf8298c.png" />
</p>

![](https://img.shields.io/github/v/release/ykinchan/ClanCoin?style=flat&logo=github)
![](https://img.shields.io/badge/licnese-MIT-brightgreen?style=flat&logo=github)
![](https://img.shields.io/github/repo-size/ykinchan/ClanCoin?style=flat&logo=github)

## Requirement
This project based on Docker. So **you have to intall Docker Desktop** on your development environment.
For more information to install Docker, please click here.
[Docker Official Docs](https://docs.docker.com/desktop/install/mac-install/)

The two `.env` files must be placed on the same level as `docker-compose.yml`.
```
== db.env ==

MYSQL_ROOT_PASSWORD=asdf
MYSQL_DATABASE=main

```
```
== backend.env ==

SECRET_KEY=<django-insecure->

DB_HOST=database      // unchangeable
DB_NAME=<dbname>
DB_USER=<db_user>
DB_PASS=<db_password>
DB_PORT=3306          // unchangeable

```


## Usage
To use ClanCoin, you can do 
```
$ git clone https://github.com/ykinchan/ClanCoin.git
$ cd ClanCoin

$ docker-compose up --build -d
or 
$ docker compose up --build -d
```
> **Note**
>The first docker compose up may fail.
>In that case, compose docker down and then compose up again.
