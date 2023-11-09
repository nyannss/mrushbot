from selenium import webdriver
from selenium.webdriver.common.by import By
from src.colors import Colors
from src.helpers import find_element_safely

def runBot (username, password):
    # Set user agent
    options = webdriver.ChromeOptions()

    # Set Custom UserAgent
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")

    # headless for hiding browser window
    options.add_argument("--headless=new")

    options.add_argument('--log-level=3')  # This sets the logging level to "silent"

    # proxy server URL
    # proxy_server_url = "182.253.63.13:8080"
    # options.add_argument(f'--proxy-server={proxy_server_url}')

    # Init browser with defined configuration
    browser = webdriver.Chrome(options=options)

    # Fetch
    browser.get("https://mrush.net")

    # Find login and password form
    username_field = browser.find_element(By.NAME, "name") 
    password_field = browser.find_element(By.NAME, "password")
    login_button = browser.find_element(By.XPATH, "//input[@type='submit'][@value='Enter']")

    # Action form
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    print(f"{Colors.OKBLUE}ℹ️ Signing in as {username}")

    error = find_element_safely(browser, By.XPATH, '//span[@class="text_red"]')
    if error:
        print(f"{Colors.FAIL}❌ {error.text}")
        exit()

    print(f"{Colors.OKGREEN}✅ Login Successful!")


    ## LAIR
    lair = find_element_safely(browser, By.XPATH, '//a[@href="/lair"]')
    if lair:
        lair.click()
        print(f"{Colors.OKGREEN}⚔️ Attacking Lair...")

        while True:
            element = find_element_safely(browser, By.PARTIAL_LINK_TEXT, 'Attack')
            if element:
                element.click()
                collectReward = find_element_safely(browser, By.PARTIAL_LINK_TEXT, 'Collect Reward')

                if(collectReward):
                    browser.refresh()
            else:
                print(f"{Colors.OKGREEN}✅ Attack Lair Done")
                break

    else:
        element = browser.find_element(By.XPATH, '//div[@id="groupTimer_index_lair"]')
        print(f"{Colors.WARNING}⏳ Lair still cooldown: \"{element.text}\"")



    ## ARENA
    try:
        arena = browser.find_element(By.XPATH, '//a[@href="/arena"]')
        arena.click()

        print(f"{Colors.OKGREEN}⚔️ Battle in Arena...")
        while True:
            element = find_element_safely(browser, By.PARTIAL_LINK_TEXT, 'Attack')
            if element:
                element.click()
            else:
                print(f"{Colors.OKGREEN}✅ Attack in Arena Done")
                break

    except:
        element = browser.find_element(By.XPATH, '//div[@id="groupTimer_index_arena"]')
        print(f"{Colors.WARNING}⏳ Arena still cooldown: \"{element.text}\"")

    exit()