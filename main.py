import uvicorn
from fastapi import FastAPI

from api_routes import anekdot_route


app = FastAPI()
app.include_router(anekdot_route)


if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8080)
