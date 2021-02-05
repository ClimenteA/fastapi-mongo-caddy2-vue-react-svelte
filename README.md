# fastapi-mongo-vue

A boilerplate for FastAPI applications. 

- FastAPI (easy async, fast and easy to use)
- Vue (but can be replaced with any other framework)
- Caddy2 (because it has automatic SSL and easy configuration)
- MongoDB 
- Redis


### How to work with this setup

Start it with: 
- `docker-compose up`

You can choose to work with either from docker containers either the usual way.
If you install new packages in local virtualenv you need to export requirements.txt and rebuild the docker containers:
- `pipenv lock -r > requirements.txt`

The same is the case for node.

Since from the frontend we need only the `dist` folder we get after running `npm run build` using docker for that it's optional. **Any frontend framework can be used**, as long it's an SPA. Make sure you add the static folders/files in `main.py` file. 


### Debug docker commands
- see logs for a particular app: `docker-compose logs -f app_fastapi`
- enter inside an app with: `docker-compose exec app_fastapi bash`
- stop a container app: `docker-compose stop app_fastapi`
- start a container app: `docker-compose up app_fastapi`



### Production setup


- Copy fontend `dist` folder to `app` folder 

Currently it's setup to work with Vuejs, but if the frontend project structure it's the same (`dist/css,img,js,index.html`) then you don't need to update static files in `main.py` file.

In progress...
