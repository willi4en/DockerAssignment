FROM python:3.10.6-slim
COPY . /home
COPY . /home/data
WORKDIR /home/data
COPY . .
RUN pip install --upgrade pip
RUN pip install Counter
CMD ["python", "./Assignment.py"]
#CMD ["pwd"]