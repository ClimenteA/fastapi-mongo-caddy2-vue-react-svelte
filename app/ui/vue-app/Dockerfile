FROM node:14

RUN mkdir -p /usr/src/ui
WORKDIR /usr/src/ui

COPY package*.json ./

RUN npm install -g @vue/cli --unsafe-perm
RUN npm install

COPY ./ ./

CMD npm run serve