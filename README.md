# NeuralNoms 🍳🤖
**NeuralNoms** is a Retrieval-Augmented Generation (RAG) chatbot that answers cooking and recipe-related questions from a custom knowledge base of recipes and cooking tips.

## 🚀 Features
- **Semantic Search:** Retrieve relevant recipes using FAISS + sentence embeddings.
- **Context-Aware Answers:** Uses a Hugging Face LLM to generate helpful cooking suggestions.
- **FastAPI Backend:** REST API for querying the chatbot.
- **Streamlit Frontend:** Clean web UI for interacting with the model.
- **Deployment-Ready:** Can be deployed for free on Hugging Face Spaces.

## 🏗️ Tech Stack
- **LLM:** Hugging Face Transformers
- **Vector DB:** FAISS
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **Deployment:** Hugging Face Spaces

## 📂 Repo Structure

src/                # Code
data/               # Knowledge base (recipes)
notebooks/          # Prototyping

## 📜 Setup
```bash
git clone https://github.com/YOUR-USERNAME/neuralnoms-rag-chatbot.git
cd neuralnoms-rag-chatbot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

🎯 Roadmap
	•	Build embedding + FAISS pipeline
	•	Create retrieval + generation function
	•	Add Streamlit UI
	•	Deploy to Hugging Face Spaces

    ---

## 🔑 Step 7: First Commit & Push

```bash
git add .
git commit -m "Initial project skeleton setup"
git push origin main