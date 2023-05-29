# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "solo_stats.py", "--server.port=8501", "--server.address=0.0.0.0"]

# Build docker image: docker build -t streamlit .
# To see image: docker images
# Run container: docker run -p 8501:8501 streamlit
# To view your app, users can browse to http://0.0.0.0:8501 or http://localhost:8501
# https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker#create-a-dockerfile