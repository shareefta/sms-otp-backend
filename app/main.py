from fastapi import FastAPI, HTTPException
from app.schemas import OTPRequest, OTPVerify
from app.services import send_otp, verify_otp

app = FastAPI()

@app.post("/send-otp")
def send_otp_route(request: OTPRequest):
    try:
        status = send_otp(request.phone)
        return {"status": status}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/verify-otp")
def verify_otp_route(request: OTPVerify):
    try:
        status = verify_otp(request.phone, request.code)
        if status == "approved":
            return {"status": "OTP verified. Login successful"}
        else:
            raise HTTPException(status_code=400, detail="Invalid OTP")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
