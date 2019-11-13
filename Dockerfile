FROM       python:3
LABEL      maintainer="haradaniel734@gmail.com"

WORKDIR    /app
COPY       . /app/

RUN        pip install -r requirements.txt
RUN        chmod a+x *.py

EXPOSE     5000

CMD        [ "python", "./main.py" ]
