FROM python

RUN pip3 install flask

WORKDIR /app

COPY . /app

EXPOSE 8123

ENTRYPOINT [ "python3" ]
CMD ["app.py"]