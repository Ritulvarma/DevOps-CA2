<img width="1920" height="1200" alt="Screenshot 2026-03-21 161713" src="https://github.com/user-attachments/assets/bb45aee7-243f-4ba3-b808-82d448cd9a4d" />
<img width="1425" height="1200" alt="Screenshot 2026-03-21 164024" src="https://github.com/user-attachments/assets/54842d51-ae6f-46f7-bfa5-32835d122ff3" />

# Student Feedback Registration Form

This project contains a Student Feedback Registration Form built with HTML, CSS, and JavaScript, along with Selenium tests and Jenkins automation.

## Files
- `index.html`: The main HTML form
- `styles.css`: External CSS styles
- `script.js`: JavaScript for form validation
- `test_form.py`: Selenium test cases

## Running the Form
Open `index.html` in a web browser.

## Running Selenium Tests
1. Ensure Python and virtual environment are set up.
2. Install dependencies: `pip install selenium webdriver-manager`
3. Run the test: `python test_form.py`

## Jenkins Setup (Windows)

### Install Jenkins
1. Download Jenkins WAR file from https://www.jenkins.io/download/
2. Ensure Java is installed (JDK 11 or later).
3. Run Jenkins: `java -jar jenkins.war` (from the directory where you downloaded it)
4. Access Jenkins at http://localhost:8080
5. Follow the setup wizard to install plugins and create admin user.

### Create a Jenkins Job
1. In Jenkins dashboard, click "New Item"
2. Enter job name: "StudentFeedbackTests"
3. Select "Freestyle project"
4. In "Source Code Management", select "None" (since local)
5. In "Build Triggers", select as needed (e.g., Build periodically)
6. In "Build", add "Execute Windows batch command"
7. Command:
   ```
   cd "c:\Users\RITUL\Downloads\DevOps CA-2"
   "c:/Users/RITUL/Downloads/DevOps CA-2/.venv/Scripts/python.exe" test_form.py
   ```
8. Save the job.
9. Click "Build Now" to run the tests.
10. Check the console output for results.

