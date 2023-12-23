from flask import Flask, render_template, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

app = Flask(__name__)

# Configure the gspread client
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/your/credentials.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet by title
spreadsheet = client.open("Your Timetable Google Sheet Title")
sheet = spreadsheet.get_worksheet(0)  # Assume the timetable is on the first sheet

@app.route('/today_schedule')
def today_schedule():
    # Get today's date
    today_date = datetime.date.today().strftime("%Y-%m-%d")

    # Get all data from the Google Sheet
    all_data = sheet.get_all_records()

    # Filter data for today's schedule
    today_schedule = [row for row in all_data if row.get('Date') == today_date]

    return render_template('today_schedule.html', today_schedule=today_schedule)

# Example API endpoint to get today's schedule in JSON format
@app.route('/api/today_schedule')
def today_schedule_api():
    today_date = datetime.date.today().strftime("%Y-%m-%d")
    all_data = sheet.get_all_records()
    today_schedule = [row for row in all_data if row.get('Date') == today_date]
    return jsonify(today_schedule)

if __name__ == '__main__':
    app.run(debug=True)
