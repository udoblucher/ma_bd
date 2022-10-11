FROM python:3.6

# set environment variables
ENV FLASK_APP run.py
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#COPY manage.py gunicorn-cfg.py requirements.txt .env ./
#COPY app app
#COPY authentication authentication
#COPY core core
#COPY customers customers

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate

#EXPOSE 5005
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
