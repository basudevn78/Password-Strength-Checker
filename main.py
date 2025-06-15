from flask import Flask, request, render_template
import re

app = Flask(__name__)

def strength_checker(password):
    if len(password) < 8:
        return "Weak Password... Must be at least 8 characters."
    if not any(char.isdigit() for char in password):
        return "Weak Password... Must include a number."
    if not any(char.isupper() for char in password):
        return "Weak Password... Must include an uppercase letter."
    if not any(char.islower() for char in password):
        return "Weak Password... Must include a lowercase letter."
    if not re.search(r'[!@#$%^&*<>.?\/,]', password):
        return "Weak Password... Must include a special character (!@#$%^&*<>.?/)"
    return " Your password is strong and secure."

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        password = request.form['password']
        result = strength_checker(password)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
