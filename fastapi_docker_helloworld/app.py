import structlog as logging
from fastapi import FastAPI
from fastapi_docker_helloworld.routes import app1, app2

logger = logging.getLogger(__name__)
app = FastAPI(title="HelloWorld")

app.include_router(app1.app)
app.include_router(app2.app)


@app.on_event("startup")
def startup():
    logger.info("HelloWrold Started!!!")
