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
