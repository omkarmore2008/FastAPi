# 
FROM python:3.9

# 
WORKDIR /app

#
COPY . /app

COPY ./requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]

