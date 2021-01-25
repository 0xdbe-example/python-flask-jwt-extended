# Python Flask JWT extended

This prototype is a Flask API protected by JWT token.

## Install

- Create a virtualenv

```
virtualenv --python=/usr/bin/python3.9 venv
source ./venv/bin/activate
```

- Install dependencies

```
pip install -r requirements.txt
```

- Run

```
export FLASK_APP=src/server.py
flask run
```

## Usage

- Get token

````
export JWT=$(curl --request POST \
  --url https://${AUTHO_TENANT}.eu.auth0.com/oauth/token \
  --header 'content-type: application/json' \
  --data '{"client_id":"${CLIENT_ID}","client_secret":"${CLIENT_SECRET}","audience":"${AUDIENCE}","grant_type":"client_credentials"}' | \
  jq -r '.access_token')
````

*for testing purpose, I get a token from Auth0 using client credentials grant flow*

- Send request on public API

```
curl http://127.0.0.1:5000/
```

- Send request on private API (Without token)

```
curl -v http://127.0.0.1:5000/user
```

*Response should be "Missing Authorization Header" with HTTP 401 UNAUTHORIZED*


- Send request on private API (With token)

```
curl -H "Authorization: Bearer JWT" http://127.0.0.1:5000/user
```
