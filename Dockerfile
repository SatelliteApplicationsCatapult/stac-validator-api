FROM python:3.8
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
# cmd gunicorn stac_validator:app on port 80
CMD ["gunicorn", "stac_validator:app" ,"--bind", "0.0.0.0:80"] 