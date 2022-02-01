FROM python:3.8.12-slim-buster
EXPOSE 8080
ARG YOUR_ENV
ENV APP_HOME=/app
WORKDIR ${APP_HOME}
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . . 
CMD streamlit run --server.port 8080 app.py
