from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

class Post (BaseModel):
    title: str
    content: str
    
    
@app.get("/")
async def root():
    return {"message": "Benim API me hosgeldin"}

@app.post("/createposts")
def create_post(new_post:Post):
    print(new_post)
    return {"data": "Post Created"}
