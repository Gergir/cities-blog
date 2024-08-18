from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.post import router as post_router
from services.db_service import Base, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(post_router)

app.mount("/images", StaticFiles(directory="images"), name="images")

Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
async def root():
    return {"message": "API is working"}
