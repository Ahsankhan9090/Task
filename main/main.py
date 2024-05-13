from fastapi import FastAPI
from main.controllers import user_controller, post_controller

app = FastAPI()

app.include_router(user_controller.router)
app.include_router(post_controller.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)