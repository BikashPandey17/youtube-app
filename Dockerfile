FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8091
CMD [ "gunicorn", "-b", "localhost:8091", "myapp.wsgi:app", "--workers=2" ]