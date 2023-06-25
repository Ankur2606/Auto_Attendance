from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from flask import Flask, render_template, request
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login_userpage.html')

@app.route('/process_login', methods=['POST','GET'])
def process_login():
    username = request.form['username']
    password = request.form['password']
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    dashboard_url = 'http://moodle.mitsgwalior.in/my/'
    driver.get(dashboard_url)
    sleep(5)

    name = driver.find_element('xpath','//*[@id="username"]')
    passcode = driver.find_element('xpath','//*[@id="password"]')

    name.send_keys(username)
    passcode.send_keys(password)

    login_button = driver.find_element('xpath','//*[@id="loginbtn"]')
    login_button.click()
    sleep(2)
    divya = driver.find_element(
    'xpath', '/html/body/div[2]/div[2]/div/div[2]/section/aside/section[2]/div/div/ul/li[13]/div/a')
    divya.click()
    sleep(2)
    attendance = driver.find_element(
    'xpath', '/html/body/div[1]/div[2]/div/div[1]/section/div/div/ul/li[3]/div[3]/ul/li[1]/div/div/div[2]/div[1]/a/span')
    attendance.click()
    sleep(2)
    while(True):
        try:
            sleep(2)
            if driver.current_url == 'http://moodle.mitsgwalior.in/login/index.php':
                name.send_keys(username)
                passcode.send_keys(password)
                sleep(3)
            Submit_ur_attendance = driver.find_element('xpath', '')
            Submit_ur_attendance.click()
            sleep(2)
            save_changes = driver.find_element(
                'xpath', '//*[@id="id_submitbutton"]')
            save_changes.click()
            sleep(2)

        except NoSuchElementException:
            print("Element not found!")
        except Exception:
            pass
        else:
            break
        finally:
            driver.refresh()
    return 'Sucessfully Implemented'

if __name__ == '__main__':
    app.run(debug = True)
