from google_calendar import *
import time

'''Delete the events with key words from the default calendar.'''
if __name__ == "__main__":
  SCOPES = ["https://www.googleapis.com/auth/calendar"]
  owis_calendarID = "19db23ca8f2295012d317da4655addab23043198bb826bb5155b94874c5a5997@group.calendar.google.com"
  my_calendarID = "private"
  my_calendar = GoogleCalendar(SCOPES)
  key_paras="This event was created by Reclaim."
  delete_event_id_list = my_calendar.show_events(paras=key_paras)
  for delete_event_id in delete_event_id_list:
    my_calendar.delete_event(delete_event_id)
    time.sleep(1) # To avoid the IO flap error from Google"