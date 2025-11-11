def generate_response(recipe, user_query):
    # placeholder "LLM-style" logic to make it read nicely
    if "error" in recipe:
        return "Hmm... I couldn't find a recipe that matches that. Try another ingredient or dish name!"

    title = recipe["title"]
    ingredients = ", ".join(recipe["ingredients"])
    steps = recipe["steps"]

    return (
        f"**{title}**\n\n"
        f"**Ingredients:** {ingredients}\n\n"
        f"**Steps:** {steps}\n\n"
        f"If you'd like, I can help you create a grocery list or suggest substitutions."
    )

'''
model = SentenceTransformer('all-MiniLM-L6-v2')

# Our sample knowledge base for NeuralNoms
knowledge_base_docs = [
    "To make a classic pesto, blend basil, pine nuts, garlic, parmesan cheese, and olive oil.",
    "A ripe avocado should yield to firm, gentle pressure but not feel mushy.",
    "The five basic tastes are sweet, sour, salty, bitter, and umami.",
    "Braising is a cooking method that uses both wet and dry heat, starting with searing and then simmering in liquid.",
    "Sourdough bread is made using a 'starter', which is a fermented culture of wild yeast and bacteria."
]

kb_embeddings = model.encode(knowledge_base_docs) # Encode the knowledge base documents

user_question = "How do I make a classic pesto?" 
question_embedding = model.encode(user_question) # Encode the user's question

scores = util.dot_score(question_embedding, kb_embeddings) # Compute similarity scores
top_doc_idx = np.argmax(scores) # Index of the most relevant document in the knowledge base

retrieved_context = knowledge_base_docs[top_doc_idx] # Retrieve the most relevant document

qa_model = pipeline("question-answering") # Initialize the question-answering pipeline
answer = qa_model(question=user_question, context=retrieved_context) # Get the answer from the QA model

print("Answer:", answer)

'''