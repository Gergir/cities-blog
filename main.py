from fastapi import FastAPI
from routers.post import router as post_router

app = FastAPI()
app.include_router(post_router)

@app.get("/")
async def root():
    return {"message": "API is working"}
