FROM node:alpine as base

WORKDIR /app

COPY challenge/package.json ./
COPY challenge/package-lock.json ./

RUN npm ci

COPY challenge .

CMD ["node", "./index.js"]