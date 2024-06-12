FROM python:slim

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

COPY repeater_dash.py .

CMD ["python", "repeater_dash.py"]


