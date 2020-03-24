FROM python:3
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
EXPOSE 80
ENTRYPOINT ["flask","run","-h","0.0.0.0","-p","80"]
