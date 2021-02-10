FROM python

COPY ./ /server/
WORKDIR /server

RUN pip3 install -r requirements.txt

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate --run-syncdb




