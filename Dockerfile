FROM python:3.10-alpine
ENV PYTHONUNBUFFERED=1
LABEL authors='nkarimi@linux.com'

WORKDIR /django-starter

COPY requirements.txt requirements.txt

RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    libffi-dev \
    && pip install uv \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

    # && uv venv venv \
    # && uv pip install --no-cache-dir -r requirements.txt



# copy app code to the container
COPY . .

EXPOSE 9000

CMD ["python", "manage.py", "runserver", "0.0.0.0:9000" ]