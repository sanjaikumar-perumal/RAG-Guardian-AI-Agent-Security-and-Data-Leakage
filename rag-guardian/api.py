#---------------------- Add the FastAPI endpoint ---------------------#


from fastapi import FastAPI
from app import security_graph

api = FastAPI(title="RAG Guardian API")

@api.get("/")
def home():
    return {"message": "RAG Guardian API is running"}

@api.post("/scan")
def run_security_scan():
    return security_graph.invoke({"results": []})

