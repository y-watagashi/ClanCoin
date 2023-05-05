# ClanCoin
ClanCoin is a payment web application for organizations. Examples of use include sending currency from parents to their children as household spending money, and from children to their parents for game time and outings.

# Installation
This project based on Docker. So **you have to intall Docker Desktop** on your development environment.
For more information to install Docker, please click here.
[Docker Official Docs](https://docs.docker.com/desktop/install/mac-install/)

# Usage
```
$ git clone https://github.com/ykinchan/ClanCoin.git
$ cd ClanCoin

$ docker-compose up --build -d
or 
$ docker compose up --build -d
```
## Usage Note
The first docker compose up <span style="color: red; "> may fail</span>.
In that case, compose docker down and then compose up again.