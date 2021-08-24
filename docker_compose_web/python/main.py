from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/db")
async def db():
    conn = psycopg2.connect(
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        password=os.environ["DB_PWD"],
    )
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users")
        return cur.fetchall()

