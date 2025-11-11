from fastapi import FastAPI
from pydantic import BaseModel

from app.retriever import RecipeRetriever
from app.model import generate_response

app = FastAPI()

# load recipes once at startup
retriever = RecipeRetriever("app/data/recipes.json")


class Query(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "NeuralNoms is live! Ask me for a recipe 🍳"}


@app.post("/chat")
def chat(query: Query):
    recipe = retriever.retrieve(query.question)
    answer = generate_response(recipe, query.question)
    return {"response": answer}