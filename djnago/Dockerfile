FROM python:3.6

EXPOSE 8000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

#RUN mkdir templates
#COPY index.html templates/
#COPY dashboard.html templates/

COPY firstjango /app
CMD python manage.py runserver 0.0.0.0:8000
