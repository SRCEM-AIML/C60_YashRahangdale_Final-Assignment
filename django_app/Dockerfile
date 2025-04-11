FROM python:3.9
ENV FLASK_ENV=development
ENV APP_NAME=flask-app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
