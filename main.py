from fastapi import FastAPI
from fastapi.params import Body
app=FastAPI()
@app.get("/") 

def read_root():
    return {"messge ": "welecme to my api !!!"}
@app.get("/posts") 
def get_posts():
    return{"data":"this is your posts"}
# The request body is automatically parsed as a Python dictionary.
# Body(...) tells FastAPI to read the JSON data from the request body.
# The client sends JSON, FastAPI converts it into a dict,
# and we can access its values using the corresponding keys.
@app.post("/createposts")
def create_posts(payload: dict = Body (...)):
    print(payload)
    return {"New_post":"title{payload}['tilte']content:{payload['content']} " }