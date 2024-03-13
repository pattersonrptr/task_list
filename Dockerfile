FROM python:3.10.12

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . .

# CMD python run.py
CMD python3 -m http.server 5000