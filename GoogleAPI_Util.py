import gspread
from oauth2client.service_account import ServiceAccountCredentials


# To define what is allowed to be accessed
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Build credentials from file
credentials = ServiceAccountCredentials.from_json_keyfile_name('OctoprintReporting-GoogleAPI-credentials.json', scope)

# Connect to Sheets API with credentials
gc = gspread.authorize(credentials)

# Build Sheet
sheet = gc.open('Octoprint Reports')

# Build report onto sheet on request
def buildOctoPrint_PrintLogs(report,sheetName):

    # Make sure worksheet exists
    if (not sheet.worksheet(sheetName)):
        worksheet = sheet.add_worksheet(title=sheetName)

    # Look at worksheet and clear it
    worksheet = sheet.worksheet(sheetName)
    worksheet.clear()

    # Add the data to the worksheet
    for row in report:
        worksheet.append_row(row)

    print('Octoprint print file logs been built - Check Google Drive!')