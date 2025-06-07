FROM python:3.12.4

WORKDIR /app
ADD . /app

RUN apt-get update && apt-get clean;

RUN pip install -r requirements.txt

ENV TZ Asia/Tokyo
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV FLASK_APP /app/app.py
ENV PYTHONPATH $PYTHONPATH:/app

ENV PORT 8080
EXPOSE 8080

CMD ["python", "app.py"]