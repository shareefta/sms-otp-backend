from pydantic import BaseModel

class OTPRequest(BaseModel):
    phone: str  # E.g., '9745xxxxxxx'

class OTPVerify(BaseModel):
    phone: str
    code: str
