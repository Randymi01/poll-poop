import keyboard
import sys
import require
from fullscreen import maximize_console
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

maximize_console()
if not require.require(['keyboard','selenium']):
    x=input()
    sys.exit()

def get_driver(url):
    driver=webdriver.Chrome()
    driver.get(url)
    print(driver)
    try:
        element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/main/form/footer/button[1]")))
    except:
        print('element not found')
    return driver

def selector(choice, driver):
    elements=[]
    try:
        for x in range(1,999):
            b='/html/body/main/form/div/ul/li[{}]/label'.format(x)
            elements.append(driver.find_element_by_xpath(b))
    except Exception as e:
        print(e)
        pass
    print(elements)
    elements[int(choice)].click()
    vote_button = driver.find_element_by_xpath("/html/body/main/form/footer/button[1]")
    vote_button.click()


while True:
    try:
        url=int(input('8 number poll value: ')
    except ValueError:
        print('\nMust be value' )
    else:
        break

url = "https://www.strawpoll.me/" + str(url)

choice = int(input('Which poll option (1,2,3,4...): '))

number = int(input('How many times would you like to manipulate this poll?: '))
for i in range(number):
    driver = get_driver(url)
    selector(choice - 1, driver)
    driver.close()
