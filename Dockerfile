FROM python:2.7.13
MAINTAINER Neil Thaker "neilthaker07@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python","app.py"]