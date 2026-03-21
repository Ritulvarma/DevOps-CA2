import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Test 1: Check whether the form page opens successfully
    driver.get("file:///c:/Users/RITUL/Downloads/DevOps%20CA-2/index.html")
    assert "Student Feedback Registration Form" in driver.title
    print("Test 1 Passed: Form page opens successfully")

    # Test 2: Enter valid data and verify successful submission
    driver.find_element(By.ID, "name").send_keys("Ritul Varma")
    driver.find_element(By.ID, "email").send_keys("ritul.varma@gmail.com")
    driver.find_element(By.ID, "mobile").send_keys("9422714321")
    driver.find_element(By.ID, "department").send_keys("Computer Science")
    driver.find_element(By.ID, "female").click()
    driver.find_element(By.ID, "comments").send_keys(
        "This is a sample feedback with more than ten words to meet the requirement."
    )
    driver.find_element(By.ID, "submitBtn").click()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert "Form submitted successfully!" in alert.text
    alert.accept()
    print("Test 2 Passed: Valid data submission")

    # Test 3: Leave mandatory fields blank and check error messages
    driver.find_element(By.ID, "resetBtn").click()
    driver.find_element(By.ID, "submitBtn").click()

    name_error = driver.find_element(By.ID, "nameError").get_attribute("textContent")
    assert "Student Name should not be empty." in name_error

    email_error = driver.find_element(By.ID, "emailError").get_attribute("textContent")
    assert "Email should be in proper format." in email_error

    mobile_error = driver.find_element(By.ID, "mobileError").get_attribute("textContent")
    assert "Mobile Number should contain 10 valid digits only." in mobile_error

    department_error = driver.find_element(By.ID, "departmentError").get_attribute("textContent")
    assert "Department should be selected." in department_error

    gender_error = driver.find_element(By.ID, "genderError").get_attribute("textContent")
    assert "At least one gender option should be selected." in gender_error

    comments_error = driver.find_element(By.ID, "commentsError").get_attribute("textContent")
    assert "Feedback Comments should not be blank and should meet minimum length of 10 words." in comments_error

    print("Test 3 Passed: Error messages for blank fields")

    # Test 4: Enter invalid email format and verify validation
    driver.find_element(By.ID, "resetBtn").click()
    driver.find_element(By.ID, "name").send_keys("Ritul Varma")
    driver.find_element(By.ID, "email").send_keys("ritul.varma@gamil.com")
    driver.find_element(By.ID, "mobile").send_keys("9422714321")
    driver.find_element(By.ID, "department").send_keys("Computer Science")
    driver.find_element(By.ID, "female").click()
    driver.find_element(By.ID, "comments").send_keys(
        "This is a sample feedback with more than ten words to meet the requirement."
    )
    driver.find_element(By.ID, "submitBtn").click()

    time.sleep(1)

    # Alert handling
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print("Alert appeared:", alert.text)
        alert.accept()
    except:
        pass

    email_value = driver.find_element(By.ID, "email").get_attribute("value")
    print(f"Email value: '{email_value}'")

    email_error = driver.find_element(By.ID, "emailError").get_attribute("textContent")
    print(f"Email error: '{email_error}'")

    assert "Email should be in proper format." in email_error
    print("Test 4 Passed: Invalid email validation")

    # Test 5: Enter invalid mobile number and verify validation
    driver.find_element(By.ID, "resetBtn").click()
    driver.find_element(By.ID, "name").send_keys("Ritul Varma")
    driver.find_element(By.ID, "email").send_keys("ritul.varma@gmail.com")
    driver.find_element(By.ID, "mobile").send_keys("123")
    driver.find_element(By.ID, "department").send_keys("Computer Science")
    driver.find_element(By.ID, "female").click()
    driver.find_element(By.ID, "comments").send_keys(
        "This is a sample feedback with more than ten words to meet the requirement."
    )
    driver.find_element(By.ID, "submitBtn").click()

    # Alert handling
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print("Alert appeared:", alert.text)
        alert.accept()
    except:
        pass

    mobile_error = driver.find_element(By.ID, "mobileError").get_attribute("textContent")
    print(f"Mobile error: '{mobile_error}'")

    assert "Mobile Number should contain 10 valid digits only." in mobile_error
    print("Test 5 Passed: Invalid mobile validation")

    # Test 6: Check dropdown
    driver.find_element(By.ID, "resetBtn").click()
    department_select = driver.find_element(By.ID, "department")
    department_select.send_keys("Information Technology")
    selected_value = department_select.get_attribute("value")
    assert selected_value == "IT"
    print("Test 6 Passed: Dropdown selection works")

    # Test 7: Reset button
    driver.find_element(By.ID, "name").send_keys("Test Name")
    driver.find_element(By.ID, "resetBtn").click()
    name_value = driver.find_element(By.ID, "name").get_attribute("value")
    assert name_value == ""
    print("Test 7 Passed: Reset button works")

    print("All tests passed!")

finally:
    driver.quit()
