FROM python:alpine

RUN pip install flask requests

COPY ./main.py /root/main.py

ENTRYPOINT ["python", "/root/main.py"]
