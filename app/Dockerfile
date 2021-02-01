FROM tiangolo/uvicorn-gunicorn:python3.8

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# install system dependencies
RUN apt-get update && apt-get clean

# upgrade pip
RUN python3 -m pip install --upgrade pip

# install requirements
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# add app
COPY . .

# run
CMD uvicorn main:app --reload --host 0.0.0.0 --port 3000

