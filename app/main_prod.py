from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv() 


import api.service_1.urls as service_1
import api.service_2.urls as service_2
import api.service_3.urls as service_3


app = FastAPI()

app.include_router(service_1.router, prefix="/api/v1/service_1")
app.include_router(service_2.router, prefix="/api/v1/service_2")
app.include_router(service_3.router, prefix="/api/v1/service_3")

@app.get("/")
async def root():
    return {'Hello': 'there!'}



# pipenv lock -r > requirements.txt
# uvicorn main:app --reload --host 0.0.0.0 --port 3000
# docker-compose up
# docker-compose exec ui (service name) bash
# docker-compose up --remove-orphans --force-recreate --build
# sudo chmod 777 dist

# Remove the need to add sudo for each docker command
# sudo groupadd docker
# sudo usermod -aG docker $USER

# Portainer (http://localhost:9000/)
# docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce

# https://docs.docker.com/engine/install/linux-postinstall/


# Remove unwanted virtualenvs
# cd /home/acmt/.local/share/virtualenvs


# LOAD TESTING 
# https://github.com/americanexpress/baton
# sudo cp baton /usr/local/bin

# DEV
# CMD uvicorn main:app --reload --host 0.0.0.0 --port 3000

# PROD
# CMD gunicorn main:app --workers=8 -b "0.0.0.0:3000" --worker-class=uvicorn.workers.UvicornWorker --log-level info


# baton -u http://localhost:3000 -c 10 -r 1000
# ====================== Results ======================
# Total requests:                                  1000
# Time taken to complete requests:         236.375341ms
# Requests per second:                             4231
# ===================== Breakdown =====================
# Number of connection errors:                        0
# Number of 1xx responses:                            0
# Number of 2xx responses:                         1000
# Number of 3xx responses:                            0
# Number of 4xx responses:                            0
# Number of 5xx responses:                            0
# =====================================================


# baton -u http://localhost:3000 -c 10 -r 10000
# ====================== Results ======================
# Total requests:                                 10000
# Time taken to complete requests:         2.526745739s
# Requests per second:                             3958
# ===================== Breakdown =====================
# Number of connection errors:                        0
# Number of 1xx responses:                            0
# Number of 2xx responses:                        10000
# Number of 3xx responses:                            0
# Number of 4xx responses:                            0
# Number of 5xx responses:                            0
# =====================================================


# baton -u http://localhost:3000 -c 10 -r 50000
# ====================== Results ======================
# Total requests:                                 50000
# Time taken to complete requests:        14.403240641s
# Requests per second:                             3471
# ===================== Breakdown =====================
# Number of connection errors:                        0
# Number of 1xx responses:                            0
# Number of 2xx responses:                        50000
# Number of 3xx responses:                            0
# Number of 4xx responses:                            0
# Number of 5xx responses:                            0
# =====================================================
