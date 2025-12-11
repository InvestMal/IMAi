from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.signals.engine import analyze_market

router = APIRouter()


# ----------- Request Schema -----------
class SignalRequest(BaseModel):
    symbol: str
    timeframe: str = "1h"
    model: str | None = None


# ----------- Endpoints -----------
@router.post("/analyze")
async def analyze_signal(data: SignalRequest):
    if not data.symbol:
        raise HTTPException(status_code=400, detail="Symbol cannot be empty")

    result = await analyze_market(
        symbol=data.symbol,
        timeframe=data.timeframe,
        model=data.model
    )

    return {"signal": result}
