import uvicorn
from fastapi import FastAPI

from api_routes import anekdot_route
from api_routes.user_routes import user_router

app = FastAPI()
app.include_router(anekdot_route)
app.include_router(user_router)


if __name__ == '__main__':
    uvicorn.run(app=app, host='127.0.0.1', port=8080)
