from twilio.rest import Client
from app.config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_VERIFY_SID

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_otp(phone: str):
    verification = client.verify.services(TWILIO_VERIFY_SID).verifications.create(
        to=f"+{phone}",
        channel="sms"
    )
    return verification.status

def verify_otp(phone: str, code: str):
    verification_check = client.verify.services(TWILIO_VERIFY_SID).verification_checks.create(
        to=f"+{phone}",
        code=code
    )
    return verification_check.status
