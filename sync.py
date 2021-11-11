from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1mhRgUBLWOJHTeTUc9uh3i7bngc64WsFLxXOImRIC4Ts'
RANGE_NAME = 'Sheet1!A2:E'

def syncSheet():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # creds = None
    # # The file token.json stores the user's access and refresh tokens, and is
    # # created automatically when the authorization flow completes for the first
    # # time.
    # if os.path.exists('token.json'):
    #     creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # # If there are no (valid) credentials available, let the user log in.
    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         # os.chdir("..")
    #         flow = InstalledAppFlow.from_client_secrets_file(
    #             'google-credentials.json', SCOPES)
    #         creds = flow.run_local_server(port=8081)
    #     # Save the credentials for the next run
    #     with open('token.json', 'w') as token:
    #         token.write(creds.to_json())

    # service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API

    #google sample for reading from spreadsheet
    # sheet = service.spreadsheets()
    # result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
    #                             range=RANGE_NAME).execute()
    # values = result.get('values', [])

    # if not values:
    #     print('No data found.')
    # else:
    #     print('Name, Major:')
    #     for row in values:
    #         # Print columns A and E, which correspond to indices 0 and 4.
    #         print('%s, %s' % (row[0], row[4]))

    values = [
    [
        34545,9,10,11
    ],
    [
        12,13,14,"goodbye"
    ]# Additional rows ...
    ]
    body = {
    'values': values
    }
    result = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME,
    valueInputOption="RAW", 
    body=body).execute()

    message= '{0} cells updated.'.format(result.get('updatedCells'))
    print(message)

    return message 

