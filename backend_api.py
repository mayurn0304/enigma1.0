from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Excel file to store usernames and passwords
EXCEL_FILE = 'user_data.xlsx'

# Create an initial Excel file with headers if it doesn't exist
try:
    pd.read_excel(EXCEL_FILE)
except FileNotFoundError:
    df = pd.DataFrame(columns=['Username', 'Password'])
    df.to_excel(EXCEL_FILE, index=False)

@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']

        # Ensure the Excel file exists
        if not pd.ExcelFile(EXCEL_FILE).sheet_names:
            df = pd.DataFrame(columns=['Username', 'Password'])
        else:
            # Load existing data from Excel
            df = pd.read_excel(EXCEL_FILE)

        # Check if the username already exists
        if username in df['Username'].values:
            return jsonify({'message': 'Username already exists'}), 400

        # Append new user to the DataFrame
        new_user = pd.DataFrame({'Username': [username], 'Password': [password]})
        df = pd.concat([df, new_user], ignore_index=True)

        # Save the updated DataFrame to Excel
        df.to_excel(EXCEL_FILE, index=False)
        print("yes")
        return jsonify({'message': 'User registered successfully'}), 201

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500


@app.route('/login', methods=['GET'])
def login_user():
    try:
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return jsonify({'message': 'Authentication failed'}), 401

        # Load existing data from Excel
        df = pd.read_excel(EXCEL_FILE)

        # Check if the username and password match
        user = df[(df['Username'] == auth.username) & (df['Password'] == auth.password)]

        if user.empty:
            return jsonify({'message': 'Invalid username or password'}), 401

        return jsonify({'message': 'Login successful'}), 200

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500
    
    
if __name__ == '__main__':
    app.run(debug=True)
