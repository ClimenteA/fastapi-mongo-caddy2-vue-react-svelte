FROM node:14


WORKDIR /usr/src/app

COPY package.json ./


RUN npm install -g vite && npm install


COPY . .


# CMD npm run dev