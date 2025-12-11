from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.ai import router as ai_router
from app.routers.signals import router as signals_router

app = FastAPI(
    title="InvestMal Enterprise AI",
    version="1.0.0",
    description="Backend API for InvestMal Enterprise Plus",
)

# ---------------------- CORS ----------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------- ROUTERS ----------------------
app.include_router(ai_router, prefix="/ai", tags=["AI"])
app.include_router(signals_router, prefix="/signals", tags=["Signals"])


# ---------------------- Root ----------------------
@app.get("/")
async def root():
    return {"status": "InvestMal AI Backend Running"}
