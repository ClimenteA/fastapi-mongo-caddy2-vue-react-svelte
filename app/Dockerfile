FROM tiangolo/uvicorn-gunicorn:python3.8

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# install system dependencies
RUN apt-get update && apt-get clean

# upgrade pip install pipenv
RUN python3 -m pip install --upgrade pip

# install requirements
# pipenv lock -r > requirements.txt
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# add app
COPY . .

# run dev
# CMD uvicorn main:app --reload --host 0.0.0.0 --port 3000

# run prod
# CMD gunicorn main:app --workers=8 -b "0.0.0.0:3000" --worker-class=uvicorn.workers.UvicornWorker --log-level info