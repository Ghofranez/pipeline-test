FROM node:20-alpine
RUN apk update && apk upgrade
WORKDIR /app

COPY package*.json ./

RUN npm install

RUN npm audit fix --force
COPY . .

EXPOSE 3000

CMD ["npm","start"]