from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///enigma_challenge.db'
db = SQLAlchemy(app)

# Model for Class Schedule
class ClassSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tutor_id = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    subject = db.Column(db.String(255), nullable=False)

# Model for Attendance
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Routes for handling various actions
@app.route('/upload_timetable', methods=['POST'])
def upload_timetable():
    if request.method == 'POST':
        file = request.files['timetable']
        # Process the uploaded timetable file
        process_timetable_upload(file)
        return "Timetable uploaded successfully"

@app.route('/specify_time_slots', methods=['POST'])
def specify_time_slots():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        preferred_slots = request.form.getlist('preferred_slots')
        # Specify time slots for the user
        specify_user_time_slots(user_id, preferred_slots)
        return "Time slots specified successfully"

@app.route('/capture_attendance', methods=['POST'])
def capture_attendance():
    if request.method == 'POST':
        class_id = request.form.get('class_id')
        student_id = request.form.get('student_id')
        status = request.form.get('status')
        # Capture attendance for the class
        capture_class_attendance(class_id, student_id, status)
        return "Attendance captured successfully"

@app.route('/send_class_notifications', methods=['POST'])
def send_class_notifications():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        message = request.form.get('message')
        # Send class notifications to the user
        send_notifications(user_id, message)
        return "Notifications sent successfully"

# Sample function to handle file upload and update the database
def process_timetable_upload(file):
    # Parse the file and extract class details
    # For simplicity, we'll assume the timetable is a CSV file with columns: tutor_id, student_id, start_time, end_time, subject
    timetable_data = file.read().decode('utf-8').splitlines()
    for line in timetable_data:
        data = line.split(',')
        tutor_id, student_id, start_time, end_time, subject = map(str.strip, data)
        start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        # Update the ClassSchedule table in the database
        class_schedule = ClassSchedule(tutor_id=tutor_id, student_id=student_id, start_time=start_time, end_time=end_time, subject=subject)
        db.session.add(class_schedule)
    db.session.commit()

# Sample function to handle time slot specification
def specify_user_time_slots(user_id, preferred_slots):
    # Update the database with the user's preferred time slots
    # For simplicity, we'll assume a User model with a time_slots field
    user = user.query.get(user_id)
    user.time_slots = ', '.join(preferred_slots)
    db.session.commit()

# Sample function to capture and record attendance
def capture_class_attendance(class_id, student_id, status):
    # Record attendance in the Attendance table
    attendance = Attendance(class_id=class_id, student_id=student_id, status=status)
    db.session.add(attendance)
    db.session.commit()

# Sample function to send notifications about scheduled classes
def send_notifications(user_id, message):
    # Implement notification logic (e.g., email, in-app notifications)
    # For simplicity, print the message to the console
    print(f"Sending notification to User {user_id}: {message}")

# Create tables if they don't exist
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)