import os
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def root():
    return {
        'status': 'ok',
        'demo_env': os.getenv('DEMO_ENV'),
    }
