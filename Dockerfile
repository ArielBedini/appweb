FROM python:3.7.10
RUN pip install Flask==2.2.2 redis==4.2
RUN useradd -ms /bis/bash admin
USER admin
WORKDIR /app
COPY app /app
CMD ["python","app.py"]
