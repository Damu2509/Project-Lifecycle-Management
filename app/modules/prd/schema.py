from pydantic import BaseModel, Field


class PRDRequest(BaseModel):
    idea: str = Field(..., min_length=3, examples=["Build an AI meeting assistant"])


class PRDResponse(BaseModel):
    validation: str
    prd: str
    suggestion: str
