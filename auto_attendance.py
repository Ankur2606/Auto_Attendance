from flask import Flask, render_template, request
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login_userpage.html')

@app.route('/process_login', methods=['POST'])
def process_login():
    username = request.form['username']
    password = request.form['password']
    
    
    return username,password

if __name__ == '__main__':
    app.run()

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

divya_attendance = 'http://moodle.mitsgwalior.in/mod/attendance/view.php?id=81999'
driver.get(divya_attendance)
sleep(3)

username,password = process_login()

name = driver.find_element('xpath','//*[@id="username"]')
passcode = driver.find_element('xpath','//*[@id="password"]')

name.send_keys(username)
passcode.send_keys(password)

login_button = driver.find_element('xpath','//*[@id="loginbtn"]')
login_button.click()
print(input())













# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# # Set the path to the WebDriver executable
# driver_path = 'C:\Users\Asus\OneDrive\Desktop\python scripting\chromedriver.exe'


# # Create a new instance of the Chrome driver
# driver = webdriver.Chrome(executable_path=driver_path)

# # Navigate to the Moodle login page
# driver.get('http://moodle.mitsgwalior.in/login/index.php')

# # Find the username input field and enter the username
# username_field = driver.find_element_by_id('username')
# username_field.send_keys(username)

# # Find the password input field and enter the password
# password_field = driver.find_element_by_id('password')
# password_field.send_keys(password)

# # Press the Enter key to submit the form
# password_field.send_keys(Keys.RETURN)

# # Alternatively, you can find the login button and click it
# # login_button = driver.find_element_by_id('loginbtn')
# # login_button.click()

# # Close the browser
# # driver.quit()


# # Set your Moodle credentials
# username = '22ml10bh686@mitsgwl.ac.in'
# password = 'Ankur@2606'
