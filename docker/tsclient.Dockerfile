FROM alpine

RUN apk add nodejs npm curl && npm install --global yarn && yarn add @switchkeys/ts-client

ENTRYPOINT [ "yarn" ]
