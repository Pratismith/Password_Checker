🔒 Password Strength Checker
A secure and interactive web app to analyze password strength, built with Flask (backend) and HTML/CSS/JavaScript (frontend).

🚀 Features
✅ Real-time password strength analysis
✅ Checks against common passwords
✅ Uses advanced security metrics
✅ Fancy UI with animated background
✅ Built with Flask, JavaScript, and Tailwind CSS

⚙️ Technologies Used
Frontend:
HTML, CSS (Tailwind), JavaScript
Fancy animations & glassmorphism UI
Backend:
Flask (Python)
REST API for password validation
Checks for common passwords, length, complexity, etc.
📥 Installation & Setup
🔹 Step 1: Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/password-checker.git
cd password-checker
🔹 Step 2: Set Up a Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
🔹 Step 3: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔹 Step 4: Run the Flask Backend
bash
Copy
Edit
python backend/app.py
Your backend will run on http://127.0.0.1:5000 🚀

🔹 Step 5: Open Frontend in Browser
Simply open index.html in your browser.

🔗 API Endpoints
Method	Endpoint	Description
POST	/check-password	Checks password strength & returns security details
Example Request (JSON)
json
Copy
Edit
{
  "password": "Pr@tismith123"
}
Example Response
json
Copy
Edit
{
  "strength": "Strong",
  "message": "Great password! It's safe to use."
}
🔒 Security Measures Implemented
✅ Checks for common passwords (Uses common_passwords.txt)
✅ Analyzes length, complexity, special characters
✅ Prevents weak passwords

🎨 UI Enhancements
Fancy animated background: "Created by Pratismith | Password Checker"
Glassmorphism design: Stylish & modern UI
Real-time strength feedback
🛠️ Future Improvements
🔹 Add password breach check using HaveIBeenPwned API
🔹 Implement dark mode toggle
🔹 Create a user authentication system

🤝 Contributing
Want to improve this project? Feel free to fork, make changes, and submit a pull request! 🚀

