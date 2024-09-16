from src.google_calendar import *
import src.get_sheets_events as get_sheets_events

'''Import calenar events into a specified calendar from the Google Sheet'''
if __name__ == "__main__":
  SCOPES = ["https://www.googleapis.com/auth/calendar", "https://www.googleapis.com/auth/spreadsheets"]
  sheetID = "1Ra359sb8kxVymyUiAYS1RyM23LzcoIux2JLVe5sRnI4"
  sheet_tab_ID = "2024-2025"
  owis_calendarID = "19db23ca8f2295012d317da4655addab23043198bb826bb5155b94874c5a5997@group.calendar.google.com"

  my_calendar = GoogleCalendar(SCOPES)
  for event in get_sheets_events.get_events(SCOPES, sheetID, sheet_tab_ID):
    print(event)
    #my_calendar.add_event(event, owis_calendarID)
