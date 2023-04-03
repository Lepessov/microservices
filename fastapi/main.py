import os

import uvicorn
from fastapi import FastAPI
import psycopg2

app = FastAPI()


@app.get('/')
def root():
    return {"message": "Hello world"}


async def get_data():
    try:
        conn = psycopg2.connect(
            dbname=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASS'),
            host=os.environ.get('DB_HOST'),
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * from dbname.users")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return {"message": data}
    except:
        return {"message": "failed"}


@app.get("/data")
async def read_data():
    data = await get_data()
    return {"data": data}



if __name__ == "__main__":
    port = 8001  # Define the port number
    uvicorn.run("main:app", host="0.0.0.0", port=port)  # Pass the port number to the uvicorn command
