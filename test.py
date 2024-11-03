import time

def test_ui(driver):
    driver.get("https://the-internet.herokuapp.com/")
    # driver.get("https://expired.badssl.com/")
    time.sleep(2)

def test_strategy(driver):
    print()
    start_time = time.time()
    driver.get("https://letcode.in/test")
    end_time = time.time()
    print(f"Time of fulfillment: {end_time - start_time}")

def test(driver):
    driver.get("https://the-internet.herokuapp.com/")
    time.sleep(5)

def test1(driver):
    print()
    locatorCSS = "a[href='/abtest']"
    locator1Xpath = "//a[@href='/abtest']"
    driver.get("https://the-internet.herokuapp.com/")
    time.sleep(2)
    print(f"Start page: {driver.current_url}")
    driver.find_element("css selector", locatorCSS).click()
    time.sleep(2)
    print(f"A/B tests page: {driver.current_url}")
    driver.back()
    print(f"Start page: {driver.current_url}")
    time.sleep(2)
    driver.forward()
    time.sleep(2)
    print(f"A/B tests page: {driver.current_url}")
    driver.refresh()

def test3(driver):
    print()
    driver.get("https://the-internet.herokuapp.com/")
    url = driver.current_url
    print(url)
    assert url == "https://the-internet.herokuapp.com/"
    title = driver.title
    print(title)
    assert title == "The Internet"

def test4(driver):
    username_loc = "input[data-test='username']"
    password_loc = "input[data-test='password']"
    login_btn_loc = "input[data-test='login-button']"
    username = "standard_user"
    password = "secret_sauce"
    check_url = "https://www.saucedemo.com/inventory.html"
    check_title = "Swag Labs"
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)
    driver.find_element("css selector", username_loc).send_keys(username)
    time.sleep(1)
    driver.find_element("css selector", password_loc).send_keys(password)
    time.sleep(1)
    driver.find_element("css selector", login_btn_loc).click()
    time.sleep(1)
    assert driver.current_url == check_url
    assert driver.title == check_title

def test5(driver):
    locator = "div[id='selectable']"
    driver.get("https://letcode.in/selectable")
    context = driver.find_elements("css selector", locator)
    for i in context:
        if i.text == "Appium":
            print(i.text)
            i.click()
            time.sleep(2)
            break
    print(context)


