# fastapi-mongo-vue

A boilerplate in progress... 

- FastAPI
- Vue (but can be replaced with any other framework)
- Caddy2 (because it has automatic SSL and easy configuration)
- MongoDB
- Redis

For now only development environment works. Needs work on production environment.

### How to work with this setup

You can choose to work with either from docker containers either the usual way.
If you install new packages in local virtualenv you need to export requirements.txt and rebuild the docker containers:
- `pipenv lock -r > requirements.txt`

The same is the case for node.