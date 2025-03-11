FROM python:3.12

LABEL maintainer="stepan.oleksiuk.dev@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

RUN useradd -m appuser
USER appuser

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
