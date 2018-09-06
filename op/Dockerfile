FROM python:3.5-alpine

RUN apk add --update --no-cache build-base libffi-dev

ADD requirements.txt /tmp/requirements.txt
RUN pip install -U pip && pip install -r /tmp/requirements.txt

ADD . /var/www/app
WORKDIR /var/www/app

EXPOSE 8000

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
