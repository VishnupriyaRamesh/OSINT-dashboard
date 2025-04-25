from flask import Flask, render_template, request
from tools import get_ip_info, get_phone_info, check_email_breach, get_website_screenshot

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    selected_option = None
    ip_result = phone_result = email_result = screenshot_url = None

    if request.method == "POST":
        selected_option = request.form.get("option")

        if selected_option == "ip":
            ip = request.form.get("ip")
            ip_result = get_ip_info(ip)

        elif selected_option == "phone":
            phone = request.form.get("phone")
            phone_result = get_phone_info(phone)

        elif selected_option == "email":
            email = request.form.get("email")
            email_result = {
                "email": email,
                "pwned_status": check_email_breach(email)
            }

        elif selected_option == "website":
            website = request.form.get("website")
            screenshot_url = get_website_screenshot(website)

    return render_template("index.html",
                           selected_option=selected_option,
                           ip_result=ip_result,
                           phone_result=phone_result,
                           email_result=email_result,
                           screenshot_url=screenshot_url)

if __name__ == "__main__":
    app.run(debug=True)
