FROM python:3.7.10
RUN useradd -ms /bis/bash admin
USER admin
WORKDIR /app
COPY requeriments.txt /app
RUN pip install --no-cache-dir -r requeriments.txt
COPY app /app
CMD ["python","app.py"]
