from fastapi import FastAPI

app = FastAPI(
    title="MeChoo", docs_url="/api/docs", openapi_url="/api"
)

@app.get("/")
def hello_world():
    return "hello world"