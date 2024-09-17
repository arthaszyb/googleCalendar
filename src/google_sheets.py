from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from src.workspace_authentication import authenticate

def get_events(SCOPES_sheets, spreadsheet_id, sheet_tab_name):
  """Reads event list from the Google Sheet."""
  #Authentication
  creds_sheets = authenticate(SCOPES_sheets)
  try:
    service = build("sheets", "v4", credentials=creds_sheets)
    # Read data from the sheet (same as previous implementation)
    sheet = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id,
                                                    range=f'{sheet_tab_name}!A1:F').execute()
    values = sheet.get('values', [])
    # Extract event data (assuming headers are in the first row)
    events = []
    headers = values[0] if values else []
    for row in values[1:]:
      event = dict(zip(headers, row))
      events.append(event)
    return events
  except HttpError as err:
      return(err)
  
