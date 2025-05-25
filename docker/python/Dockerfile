FROM python:3.10.12

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY . .

ENTRYPOINT ["python"]
CMD ["main.py"]
