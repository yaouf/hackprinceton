# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from google.oauth2 import service_account
from googleapiclient.discovery import build
from config import GOOGLE_CALENDAR_ID
from calendar_utils import parse_event, create_event_in_calendar

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Use a secure key in production

# Load Google API credentials and initialize calendar service
credentials = service_account.Credentials.from_service_account_file("credentials.json")
service = build("calendar", "v3", credentials=credentials)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form.get("prompt")
        event_data = parse_event(prompt)

        # Render the confirmation page with parsed event details
        return render_template("confirm.html", event_data=event_data)

    return render_template("index.html")

@app.route("/confirm", methods=["POST"])
def confirm():
    # Confirm event creation
    event_data = request.form.to_dict()
    event = create_event_in_calendar(service, event_data)

    flash("Event created successfully!")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
