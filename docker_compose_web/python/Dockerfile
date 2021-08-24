FROM continuumio/miniconda3:4.10.3-alpine

RUN conda install -c defaults -c conda-forge \
	fastapi \
	uvicorn \
	psycopg2
COPY main.py /app/
WORKDIR /app

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0" ]