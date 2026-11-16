from fastapi import FastAPI

app = FastAPI(
    title="SentinelOps API",
    description="Automated Vulnerability Management & SOAR Platform",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "SentinelOps Core Engine"}
