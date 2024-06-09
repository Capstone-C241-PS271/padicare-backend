FROM python:3.10.12-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./

ENV BASE_PATH=/usr/src/app

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]

EXPOSE 8080
