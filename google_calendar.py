import datetime

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from workspace_authentication import authenticate

class GoogleCalendar():
  """A class to manage events in Google Calendar."""

  def __init__(self, auth_scope):
    self.creds = authenticate(auth_scope)
    try:
      self.service = build("calendar", "v3", credentials=self.creds)
    except HttpError as err:
      print(err)

  def list_calendars(self):
    '''List all the calendars and print out.'''
    page_token = None
    while True:
      calendar_list = self.service.calendarList().list(pageToken=page_token).execute()
      for calendar_list_entry in calendar_list['items']:
        print(calendar_list_entry['summary'])
      page_token = calendar_list.get('nextPageToken')
      if not page_token:
        break

  def add_event(self, event, calendarID="primary"):
    """Creates a new event in Google Calendar."""
    # Extract event details
    start_date = event['Start Date']
    end_date = event['End Date']
    title = event['Title']
    description = event.get('Description', '')

    # Prepare event body
    event_body = {
        'summary': title,
        'description': description,
        'start': {
            'date': start_date,
        },
        'end': {
            'date': end_date,
        },
    }

    try:
      event = self.service.events().insert(calendarId=calendarID, body=event_body).execute()
      print(f"Event created: {event.get('htmlLink')}")
    except HttpError as error:
      print(f"An error occurred adding event: {error}")

  def delete_event(self, event_id, calendarID="primary"):
    """Deletes an event from Google Calendar based on its ID."""
    try:
      self.service.events().delete(calendarId=calendarID, eventId=event_id).execute()
      print(f"Event deleted: {event_id}")
    except HttpError as error:
      print(f"An error occurred deleting event: {error}")

  def show_events(self, calendar="primary", start_date=None, end_date=None, paras=None):
    """Shows events from Google Calendar based on optional date range."""
    # Prepare query parameters
    params = {}
    if start_date:
      params['timeMin'] = datetime.datetime.strptime(start_date, '%Y-%m-%d').isoformat() + 'Z'
    if end_date:
      params['timeMax'] = datetime.datetime.strptime(end_date, '%Y-%m-%d').isoformat() + 'Z'
    if paras:
      params["q"] = paras

    # Get events
    try:
      events = self.service.events().list(calendarId=calendar, singleEvents=True, **params).execute().get('items', [])
      event_id_list = []
      if events:
        for event in events:
          event_id_list.append(event['id'])
          print(event['id'])
          print(f"Event: {event['summary']}")
          print(f"  - Start: {event['start'].get('dateTime', event['start'].get('date'))}")
          print(f"  - End:   {event['end'].get('dateTime', event['end'].get('date'))}")
          if 'description' in event:
            print(f"  - Description: {event['description']}")
    except Exception as e:
      print(e)
    else:
        print("No events")
    return event_id_list
    
