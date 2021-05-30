FROM python:alpine3.13
COPY . /app
WORKDIR /app
RUN apk update && apk add --no-cache supervisor
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 8091
CMD ["/usr/bin/supervisord"]