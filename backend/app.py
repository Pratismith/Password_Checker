from flask import Flask, request, jsonify
from flask_cors import CORS
from password_checker import analyze_password

app = Flask(__name__)
CORS(app)

@app.route('/check-password', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password', '')

    if not password:
        return jsonify({'error': 'Password is required'}), 400

    result = analyze_password(password)

    if result["pwned_count"] > 0:
        result["message"] = f"⚠️ This password has been found in {result['pwned_count']} breaches! Choose another one."
    elif result["common"]:
        result["message"] = "⚠️ This is a common password. Avoid using it!"
    elif result["strength"] == "Weak":
        result["message"] = "❌ Your password is weak. Try making it longer with special characters!"
    elif result["strength"] == "Moderate":
        result["message"] = "✅ Your password is okay, but adding more variety can make it stronger."
    else:
        result["message"] = "✅ Your password is strong! Good job!"

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
