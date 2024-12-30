from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Mock credentials (for testing only)
MOCK_CREDENTIALS = {
    "test_user": "securepassword"
}

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    # Simulate a timing-based response
    if username in MOCK_CREDENTIALS:
        for i, (char1, char2) in enumerate(zip(password, MOCK_CREDENTIALS[username])):
            if char1 != char2:
                time.sleep(0.1 * (i + 1))  # Simulate timing leak
                return jsonify({"message": "Invalid password"}), 401
        
        if password == MOCK_CREDENTIALS[username]:
            return jsonify({"message": "Login successful"}), 200
    
    time.sleep(0.1)  # Add a default delay for unknown usernames
    return jsonify({"message": "Invalid username"}), 401

if __name__ == "__main__":
    app.run(debug=True)
