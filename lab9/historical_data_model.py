from typing import List
from pydantic import BaseModel, Field, RootModel, validator
from datetime import datetime

class HistoricalData(BaseModel):
    time: datetime
    low: float = Field(..., gt=0)
    high: float = Field(..., gt=0)
    open: float = Field(..., gt=0)
    close: float = Field(..., gt=0)
    volume: float = Field(..., ge=0)

    @validator('time', pre=True)
    def parse_time(cls, value):
        if isinstance(value, int):
            return datetime.fromtimestamp(value)
        return value

class HistoricalDataList(RootModel):
    root: List[HistoricalData]
