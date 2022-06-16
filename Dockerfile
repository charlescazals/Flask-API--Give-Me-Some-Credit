FROM python:3.7.1

COPY . .

RUN pip3 install -r requirements.txt

CMD flask run --host=0.0.0.0
