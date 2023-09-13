# 
FROM python:3.9

# 
WORKDIR /app


COPY ./requirements.txt /app/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker main:app"]
