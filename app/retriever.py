import json
from sentence_transformers import SentenceTransformer, util


class RecipeRetriever:
    def __init__(self, recipe_file: str):
        # Load recipe data
        with open(recipe_file, "r") as f:
            self.recipes = json.load(f)

        # Load embedding model (runs on CPU)
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

        # Pre-compute embeddings for faster retrieval
        self.recipe_texts = [
            recipe["title"] + " " + " ".join(recipe["ingredients"]) + " " + recipe["steps"]
            for recipe in self.recipes
        ]
        self.embeddings = self.model.encode(self.recipe_texts, convert_to_tensor=True)

    def retrieve(self, query: str):
        query_embedding = self.model.encode(query, convert_to_tensor=True)

        # Compute similarity scores
        scores = util.cos_sim(query_embedding, self.embeddings)[0]

        # Get index of best match
        best_idx = int(scores.argmax())

        best_recipe = self.recipes[best_idx]
        return best_recipe