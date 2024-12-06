FROM python:3.9

WORKDIR /usr/src/app

WORKDIR /app
COPY . /app
COPY tests/ ./tests/
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app/app.py

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]