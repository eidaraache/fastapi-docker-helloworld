from fastapi import APIRouter


app = APIRouter()


@app.get("/hallowelt")
def hallowelt():
    return "hallo welt"
