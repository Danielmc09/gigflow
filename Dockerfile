FROM python:3.9

ENV PYTHONUNBUFFERED=1

COPY . /app

WORKDIR /app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

#RUN python manage.py makemigrations
#RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
