# Hosting the bot yourself setup

## Option 1: Running it as a simple python application

Prerequistes:<br>
a) Install the requirements: ```pip install -r requirements.txt```<br>

b) Create a discord bot using the developer platform of discord and obtain your **OAuth2 token**. Keep it somewhere safe

c) Create a database folder in the Bot directory

d) Export the token as an environment variable: ```export TOKEN=<OAUTH TOKEN>``` and ```export PREFIX=<Desired default prefix of bot>```

e) Go into the Bot directory and then run: ```python bot.py```

f) Get the bot invite link from the discord developer platform and invite them to your desired servers!


## Option 2: Running it as a docker container
a) Create a discord bot using the developer platform of discord and obtain your **OAuth2 token**. Keep it somewhere safe

b) In the ```docker-compose.yml``` file at line 12 change the ```TOKEN``` variable with the OAUTH token you received above.
The line should look like this: ```- TOKEN=YOUR OAUTH TOKEN```. At line 13 change ```PREFIX``` variable with the desired default prefix of the bot. The line should like this: <br>```-PREFIX=<PREFIX>```.

c) Create a ```database``` folder in the root directory.

d) Now to run the container simply run:
```docker-compose up --build```

e) Get the bot invite link from the discord developer platform and invite them to your desired servers!


## To get exisiting published comics in your database
a) Install ```requirements.txt``` and then run ```scraper.py```. It will scrape http://pt.jikos.cz/garfield/ and get all the comics available
