# FastApi + Vue/React/Svelte + MongoDB


### How to work with this setup

Start it with: 
- `docker-compose up`






A boilerplate for FastAPI applications. 

- FastAPI (easy async, fast and easy to use)
- Vue (but can be replaced with any other framework)
- Caddy2 (because it has automatic SSL and easy configuration)
- MongoDB 
- Redis


You can choose to work with either from docker containers either the usual way.
If you install new packages in local virtualenv you need to export requirements.txt and rebuild the docker containers:
- `pipenv lock -r > requirements.txt`

The same is the case for node.

Since from the frontend we need only the `dist` folder we get after running `npm run build` using docker for that it's optional. **Any frontend framework can be used**, as long it's an SPA. Make sure you add the static folders/files in `main.py` file. 


### Manage docker with Portainer 
- Install portainer with: `docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce`
- Web interface will be at: `http://localhost:9000/`


### Debug docker commands
- see logs for a particular app: `docker-compose logs -f app_fastapi`
- enter inside an app with: `docker-compose exec app_fastapi bash or \bin\sh for alpine versions`
- stop a container app: `docker-compose stop app_fastapi`
- start a container app: `docker-compose up app_fastapi`
- Delete unwanted virtualenvs: `cd /home/acmt/.local/share/virtualenvs` (ubuntu)
- DEV start: `uvicorn main:app --reload --host 0.0.0.0 --port 3000`
- PROD start: `gunicorn main:app --workers=8 -b "0.0.0.0:3000" --worker-class=uvicorn.workers.UvicornWorker --log-level info`
- Change permision of a file/folder: `sudo chmod 777 dist`
- Remove the need to add `sudo` for each docker command: `sudo groupadd docker` and `sudo usermod -aG docker $USER`





### Production setup


- Copy fontend `dist` folder to `app` folder 

Currently it's setup to work with Vuejs, but if the frontend project structure it's the same (`dist/css,img,js,index.html`) then you don't need to update static files in `main.py` file.

In progress...
