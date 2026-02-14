from fastapi import FastAPI
from pydantic import BaseModel

from app.retriever import RecipeRetriever
from app.model import generate_response

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# load recipes once at startup
retriever = RecipeRetriever("app/data/recipes.json")


class Query(BaseModel):
    question: str

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/chat-ui")
def chat_ui():
    return FileResponse("static/index.html")

@app.get("/")
def home():
    return {"message": "NeuralNoms is live! Ask me for a recipe 🍳"}


@app.post("/chat")
def chat(query: Query):
    recipe = retriever.retrieve(query.question)
    answer = generate_response(recipe, query.question)
    return {"response": answer}