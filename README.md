# FastApi + Vue/React/Svelte + MongoDB

A simple boilerplate for FastAPI single page applications. 

There are 2 environments available one for production with `Caddy2` as a reverse proxy and one for development.

You can choose to work with docker containers or not.

In the `app` folder we have the `FastAPI` code. Make sure to add all dependencies in `requirements.txt`.
In the `ui` folder we have 3 boilerplate folders created with `vite` (Vue, React, Svelte). 



# Development

- CD in the `app` folder and start the `FastAPI` with  `uvicorn main:app --reload --host 0.0.0.0 --port 5000` (see the api at `localhost:5000`);
- CD in the `ui/your-prefered-framework` folder and start the ui with `npm run dev` (see the frontend at `localhost:3000`);

You can change the folder structure as you want. 
This setup is focused on making simple, easy to modify production and development environment.


# Production

Update `Caddyfile` with:
- a valid email(used for https);
- a valid domain name in place of localhost;
- update `.env` file as needed (you may need to change `UI_DIST_DIR=/ui/svelte-app/dist` with your choosed frontend framework);
- run `npm run build` to let `vite` generate the `dist` folder.


Notice in the `docker-compose.prod.yml` that we didn't exposed any ports only `Caddy2` will handle interaction with the outside world.

When the root of the domain name will be accessed, `index.html` file will be served.





## Utils

- Remove the need to add `sudo` for each docker command: `sudo groupadd docker` and `sudo usermod -aG docker $USER`
- Install portainer with: `docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce`
- Web interface will be at: `http://localhost:9000/`
- see logs for a particular app: `docker-compose logs -f container_name`
- enter inside an app with: `docker-compose exec container_name bash or \bin\sh for alpine versions`
- stop a container app: `docker-compose stop container_name`
- start a container app: `docker-compose up container_name`
- Delete unwanted virtualenvs: `cd /home/user/.local/share/virtualenvs` (ubuntu)
- DEV start: `uvicorn main:app --reload --host 0.0.0.0 --port 3000`
- PROD start: `gunicorn main:app --workers=8 -b "0.0.0.0:3000" --worker-class=uvicorn.workers.UvicornWorker --log-level info`
