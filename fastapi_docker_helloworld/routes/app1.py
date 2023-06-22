from fastapi import APIRouter


app = APIRouter()


@app.get("/helloworld")
def helloworld():
    return "hello world"
