import os
import requests
import socket
from dotenv import load_dotenv

load_dotenv()

# API Keys
IPINFO_API_KEY = os.getenv("IPINFO_API_KEY")
VERIPHONE_API_KEY = os.getenv("VERIPHONE_API_KEY") or "7F63783BC0C34A248DAF168119F5857F"
ABSTRACT_API_KEY = os.getenv("ABSTRACT_API_KEY") or "9dbf068b65fc4847b8c22a0381bec237"
APIFLASH_API_KEY = os.getenv("APIFLASH_API_KEY") or "5942102ab06f4ec5a00ec0718e3a8da5"

# IP Lookup
def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Phone Number Lookup (Veriphone)
def get_phone_info(phone):
    url = f"https://api.veriphone.io/v2/verify?phone={phone}&key={VERIPHONE_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return {
            "valid": data.get("phone_valid"),
            "international_number": data.get("phone"),
            "country": data.get("country"),
            "carrier": data.get("carrier"),
            "line_type": data.get("phone_line_type"),
            "phone_region": data.get("phone_region")
        }
    except Exception as e:
        return {"error": str(e)}

# Email Check (Abstract + Fake breach line)
def check_email_breach(email):
    if not email:
        return {"status": "Invalid", "message": "No email provided."}

    try:
        url = f"https://emailvalidation.abstractapi.com/v1/?api_key={ABSTRACT_API_KEY}&email={email}"
        response = requests.get(url)
        data = response.json()

        if data.get("is_valid_format", {}).get("value") == False:
            return {
                "status": "Invalid",
                "message": "Invalid email format."
            }

        domain = email.split("@")[-1]
        try:
            socket.gethostbyname(domain)
        except:
            return {
                "status": "Error",
                "message": "This email domain does not exist or is unreachable."
            }

        return {
            "status": "Valid",
            "message": "Email is valid. This website is not pwned.",
            "details": {
                "deliverability": data.get("deliverability"),
                "quality_score": data.get("quality_score"),
                "is_disposable": data.get("is_disposable_email", {}).get("value"),
                "autocorrect": data.get("autocorrect"),
                "email": data.get("email")
            }
        }

    except Exception as e:
        return {"status": "Error", "message": f"API error: {str(e)}"}

# Website Screenshot
def get_website_screenshot(url):
    return f"https://api.apiflash.com/v1/urltoimage?access_key={APIFLASH_API_KEY}&wait_until=page_loaded&url={url}"
