import dateparser
from datetime import timedelta  # Import timedelta to resolve the NameError
from googleapiclient.errors import HttpError

def parse_event(prompt):
    """Parses the event details from the provided prompt."""
    # Placeholder parsing logic (expand as needed)
    title, time, location = "Sample Event", "5pm", "CIT 101"  # Example data (you should expand this to parse real data from prompt)
    
    # Parse the provided time using dateparser
    parsed_time = dateparser.parse(time)  # Parses time in natural language

    # Return event details with parsed start and end times
    return {
        "summary": title,
        "start": {"dateTime": parsed_time.isoformat(), "timeZone": "America/New_York"},
        "end": {"dateTime": (parsed_time + timedelta(hours=1)).isoformat(), "timeZone": "America/New_York"},
        "location": location
    }

def create_event_in_calendar(service, event_data):
    """Creates an event in the user's Google Calendar."""
    try:
        event = service.events().insert(calendarId="primary", body=event_data).execute()
        return event
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None
