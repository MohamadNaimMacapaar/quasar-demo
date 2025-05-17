# main.py
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from bson.objectid import ObjectId

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["theses"]

# Allow CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/theses")
def get_theses():
    return [{**doc, "_id": str(doc["_id"])} for doc in collection.find()]

@app.post("/theses")
def add_thesis(thesis: dict):
    result = collection.insert_one(thesis)
    return {"inserted_id": str(result.inserted_id)}

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    title: str = Form(...),
    description: str = Form(...),
    groupMembers: str = Form(...),
    category: str = Form(...)  # <-- add this
):
    import json
    group_members = json.loads(groupMembers)
    contents = await file.read()
    doc = {
        "title": title,
        "description": description,
        "groupMembers": group_members,
        "filename": file.filename,
        "category": category,  # <-- save category
        "approval": "Pending", # default value
        "status": "In Progress", # default value
        # "color": "#ffe6ea", # optional, for card color
    }
    collection.insert_one(doc)
    return {"message": "Upload successful"}