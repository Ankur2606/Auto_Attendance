from selenium import webdriver
from time import sleep
from flask import Flask, render_template, request
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

# Create a Flask app
app = Flask(__name__)

# Define the login route
@app.route('/')
def login():
    """This route renders the login page."""
    return render_template('login_userpage.html')

# Define the process_login route
@app.route('/process_login', methods=['POST','GET'])
def process_login():
    """This route handles the login process."""

    # Get the username and password from the request form
    username = request.form['username']
    password = request.form['password']

    # Create a new Chrome driver
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    # Go to the Moodle dashboard
    dashboard_url = 'http://moodle.mitsgwalior.in/my/'
    driver.get(dashboard_url)
    sleep(5)

    # Find the username and password input fields
    name = driver.find_element_by_xpath('//*[@id="username"]')
    passcode = driver.find_element_by_xpath('//*[@id="password"]')

    # Enter the username and password
    name.send_keys(username)
    passcode.send_keys(password)

    # Find the login button and click it
    login_button = driver.find_element_by_xpath('//*[@id="loginbtn"]')
    login_button.click()
    sleep(2)

    # Find the Bhagat link and click it
    bhagat = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/section/div/aside/section[5]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div[4]/div[1]/div/div[1]/a/span[3]')
    bhagat.click()
    sleep(2)

    # Find the attendance link and click it
    attendance = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/section/div/div/ul/li[3]/div[3]/ul/li[4]/div/div/div[2]/div[1]/a/span')
    attendance.click()

    # Keep looping until the user is logged in or the login page is no longer displayed
    while True:
        try:
            # Check if the current URL is the login page
            if driver.current_url == 'http://moodle.mitsgwalior.in/login/index.php':
                # The user is not logged in, so send the username and password again
                name.send_keys(username)
                passcode.send_keys(password)
                sleep(3)
           # Find the button to submit attendance.
            Submit_ur_attendance = driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[1]/section/div[1]/table[1]/tbody/tr[1]/td[3]/a')

            # Click the button to submit attendance.
            Submit_ur_attendance.click()

            # Wait for the page to load.
            sleep(2)

            # Find the radio button for "Present".
            Present = driver.find_element('xpath','/html/body/div[1]/div[2]/div/div[1]/section/div[1]/form/fieldset/div/div/div[2]/fieldset/div/label[1]/span')

            # Click the radio button for "Present".
            Present.click()

            # Wait for the page to load.
            sleep(2)

            # Find the button to save changes.
            save_changes = driver.find_element('xpath', '//*[@id="id_submitbutton"]')

            # Click the button to save changes.
            save_changes.click()
        except Exception:
            # An unexpected error occurred, so print the stack trace
            pass
        else:
            # The loop should only reach this point if the login was successful
            break

        finally:
            driver.refresh()
    return 'Sucessfully Implemented'

if __name__ == '__main__':
    app.run(debug = True)
