# from selenium import webdriver
from seleniumwire import webdriver as wdriverwire
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.colors import Colors
from src.helpers import find_element_safely
import csv
import random
import ua_generator

def runBot (username, password, proxy=False):
    # Set user agent
    try:
        print(f"{Colors.OKBLUE}ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️")

        options = webdriver.ChromeOptions()

        # Set Custom UserAgent
        user_agent = ua_generator.generate()
        # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36"
        options.add_argument(f"user-agent={user_agent}")
        print(f"{Colors.OKBLUE}ℹ️ User-Agent: {user_agent}")


        # Disable load image for load faster
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)

        # headless for hiding browser window
        options.add_argument("--headless=new")

        options.add_argument('--log-level=3')  # This sets the logging level to "silent"

        if proxy:
            # proxy server URL
            proxies = []

            with open('proxies.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    proxies.append({
                        'username': row['username'].strip(),
                        'password': row['password'].strip(),
                        'host': row['host'].strip(),
                        'port': row['port'].strip()
                    })

            # Get a random proxy
            random_proxy = random.choice(proxies)

            # Access the proxy details
            p_username = random_proxy['username']
            p_password = random_proxy['password']
            p_host = random_proxy['host']
            p_port = random_proxy['port']
            p_auth = f'{p_username}:{p_password}@' if username and password else ''

            seleniumwire_options = {
                'proxy': {
                    'http': f'http://{p_auth}{p_host}:{p_port}',
                    'http': f'https://{p_auth}{p_host}:{p_port}',
                    'verify_ssl': False,
                },
            }
            

            # Init browser with defined configuration
            browser = wdriverwire.Chrome(options=options, seleniumwire_options=seleniumwire_options)
            print(f"{Colors.OKBLUE}ℹ️ Connecting server with proxy: {p_host}:{p_port}")

        else:

            browser = webdriver.Chrome(options=options)
            print(f"{Colors.OKBLUE}ℹ️ Connecting server with current ip")


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

        ## CLAN LAIR
        try:
            cl_time = browser.find_element(By.XPATH, '//div[@id="groupTimer_index_clan_lair"]')

            clan_lair = find_element_safely(browser, By.XPATH, '//a[@href="/clan_lair"]')

            if clan_lair:
                clan_lair.click()
                
                print(f"{Colors.OKGREEN}⚔️  Battle in Clan Lair...")

                locked = find_element_safely(browser, By.XPATH, '//span[@class="lose"]')
                if locked:
                    print(f"{Colors.WARNING}😒 Can't participate in clan lair: {locked.text}")
                else:
                    while True:
                        cl_attack = find_element_safely(browser, By.PARTIAL_LINK_TEXT, 'Attack')
                        if cl_attack:
                            cl_attack.click()
                        else:
                            print(f"{Colors.OKGREEN}✅ Attack in Clan lair done")
                            break
            else:
                print(f"{Colors.WARNING}⏳ Clan lair still cooldown: \"{cl_time.text}\"")

        except:
            print(f"{Colors.WARNING}😒 Clan lair isn't open")

        ## Task
            print(f"{Colors.OKGREEN}📜 Checking task")
        browser.get('https://mrush.net/task/daily')
        try:
            while True:
                element = browser.find_element(By.PARTIAL_LINK_TEXT, 'Collect')
                element.click()
                print(f"{Colors.OKGREEN}✅ Complete the Task")


        except:
            print(f"{Colors.WARNING}😒 No completed quests left")



    except:
        print(f"{Colors.FAIL}❌ Cannot make connection to server")

    finally:
        browser.quit()

    exit()