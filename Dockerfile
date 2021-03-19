FROM python:latest

COPY requirements.txt ./requirements.txt
COPY std.py ./std.py
COPY server.py ./server.py

RUN pip install -r requirements.txt
CMD ["python", "./server.py"]