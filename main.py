from src.google_calendar import *
import src.google_sheets as google_sheets
from src.utils import load_conf
import time

def add_event_cmd(sheetID, sheet_tab_ID, calendarId):
    '''Import calendar events into a specified calendar from the Google Sheet'''
    for event in google_sheets.get_events(SCOPES, sheetID, sheet_tab_ID):
        print(event)
        #my_calendar.add_event(event, calendarId)

def delete_calendar_event_cmd(key_paras, calendarId):
    '''Delete the events from calendar by particular key words'''
    delete_event_id_list = my_calendar.show_events(paras=key_paras)
    for delete_event_id in delete_event_id_list:
        my_calendar.delete_event(delete_event_id)
        time.sleep(1) # To avoid the IO flap error from Google"

#main
if __name__ == "__main__":
    conf = load_conf('conf/conf.json')
    calendar_conf, sheet_conf = conf.get('calendar_conf'), conf.get('sheet_conf')
    SCOPES = [calendar_conf.get('calendar_access'), sheet_conf.get('sheets_access')]
    sheetID = sheet_conf.get('sheet_ID')
    sheet_tab_ID = sheet_conf.get("sheet_name")
    owis_calendarID = calendar_conf.get('owis_calendarID')
    my_calendarID = calendar_conf.get('default_calendarID')
    key_paras="This event was created by Reclaim."
    
    my_calendar = GoogleCalendar(SCOPES)
    #delete_calendar_event_cmd(key_paras, my_calendarID)
    add_event_cmd(sheetID, sheet_tab_ID, owis_calendarID)


  
