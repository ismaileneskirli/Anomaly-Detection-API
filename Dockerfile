FROM python:latest

RUN mkdir /app/
WORKDIR /app/
COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8008


ENTRYPOINT [ "python" ]
CMD [server.py]