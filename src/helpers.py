def find_element_safely(driver, by, value):
    try:
        element = driver.find_element(by, value)
        return element
    except:
        return None