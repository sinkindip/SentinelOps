from fastapi import FastAPI
from app.db.session import engine, Base
from app.db import models

# Create database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SentinelOps API",
    description="Automated Vulnerability Management & SOAR Platform",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "SentinelOps Core Engine",
        "database": "connected"
    }
