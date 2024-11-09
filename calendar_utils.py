# calendar_utils.py
import dateparser
from googleapiclient.errors import HttpError

def parse_event(prompt):
    # Example of parsing logic (expand as needed)
    title, time, location = "Sample Event", "5pm", "CIT 101"  # Placeholder parsing
    parsed_time = dateparser.parse(time)  # Parses time in natural language

    return {
        "summary": title,
        "start": {"dateTime": parsed_time.isoformat(), "timeZone": "America/New_York"},
        "end": {"dateTime": (parsed_time + timedelta(hours=1)).isoformat(), "timeZone": "America/New_York"},
        "location": location
    }

def create_event_in_calendar(service, event_data):
    try:
        event = service.events().insert(calendarId="primary", body=event_data).execute()
        return event
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None
