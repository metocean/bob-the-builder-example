FROM python:alpine

RUN pip install flask

COPY ./main.py /root/main.py

EXPOSE 8080

ENTRYPOINT ["python", "/root/main.py"]
