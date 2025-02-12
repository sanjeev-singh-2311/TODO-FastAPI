from fastapi import FastAPI
from app.routes import app_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins=[
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(app_router)

if __name__ == "__main__":
    import uvicorn
    try:
        uvicorn.run(app, host="0.0.0.0", port=8800)
        print("Server started")
    except:
        print("Server failed")
