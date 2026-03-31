FROM node:20-alpine

RUN apk update && apk upgrade

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN adduser -D appuser
USER appuser

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://localhost:3000 || exit 1

CMD ["npm", "start"]