from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse  # Import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from app.model.model import predict_pipeline, __version__ as model_version
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve(strict=True).parent
templates = Jinja2Templates(directory=f"{BASE_DIR}/templates")

class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    language: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "model_version": model_version})

@app.post("/predict", response_model=PredictionOut)
async def predict(request: Request, document: TextIn):
    payload = await request.json()
    language = predict_pipeline(payload["text"])
    return {"input": payload["text"], "language": language}
