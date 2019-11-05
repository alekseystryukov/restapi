FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev  musl-dev \
  && apk add postgresql-dev
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

RUN addgroup -S django && adduser -S -G django django
RUN chown -R django /app
USER django

#HEALTHCHECK --interval=1m --timeout=5s --retries=2 --start-period=10s \
#  CMD wget -qO- http://0.0.0.0:8000/healthcheck/ || exit 1

ENTRYPOINT ["/app/entrypoint.sh"]
