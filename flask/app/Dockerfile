FROM python:3.6

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

RUN mkdir templates
COPY index.html templates/
COPY dashboard.html templates/

COPY app.py /app
CMD python app.py
