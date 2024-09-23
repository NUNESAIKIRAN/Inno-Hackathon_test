from flask import Flask, request, render_template
import re
import os

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/results", methods=['POST'])
def results():
    test_string = request.form.get("test_string")
    regex = request.form.get("regex")

    matches = []

    if test_string and regex:
        try:
            compiled_pattern = re.compile(regex)
            matches = compiled_pattern.findall(test_string)
            print("Matches found:", matches)
        except re.error:
            matches = ['Invalid Regex Pattern']
            print("Error in regex pattern")
    else:
        matches = ["Both test string and regex are required"]
        print("Test string or regex not provided")

    return render_template("index.html", test_string=test_string, regex=regex, matches=matches)

@app.route("/validation_email", methods=['POST', 'GET'])
def validation():
    email = None
    is_valid = None
    
    if request.method == "POST":
        email = request.form.get("email")
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        is_valid = re.match(email_regex, email) is not None

    # Handle both GET and POST cases by rendering the same template with default or POST values
    return render_template("validation.html", email=email, is_valid=is_valid)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)

