from selenium import webdriver
from selenium.webdriver.common.by import By



def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-link-features=AutomationControlled")
  
    # Specify the path to the chromedriver executable
    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver

def main():
    driver = get_driver()
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")
    return element

print(main())
