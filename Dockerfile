FROM python:3.7
COPY ./ /usr/src/app
WORKDIR /usr/src/app
RUN pip3 install flask
RUN pip3 install Flask-APScheduler
EXPOSE 5000
CMD [ "python3", "app.py" ]
