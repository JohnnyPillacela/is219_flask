FROM python:3.8-buster
COPY requirements.txt .
ENV FLASK_APP=flaskr
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV PATH="/home/myuser/.local/bin:${PATH}"
RUN apt-get update &&\
    /usr/local/bin/python3 -m pip install -r requirements.txt &&\
    /usr/local/bin/python3 -m pip install --upgrade pip &&\
    python -m pip install --upgrade setuptools &&\
    adduser myuser
WORKDIR /home/myuser
COPY --chown=myuser:myuser . .
#RUN flask init-db
#CMD ["uwsgi", "app.ini"]
CMD ["flask", "run"]