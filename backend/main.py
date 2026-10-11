from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/upload-files")
async def send_message():
    return {"message": "This is test"}


@app.get("/home")
async def get_data(query: str = ""):
    return {"message": f"Backend received: {query}" if query else "Welcome"}
