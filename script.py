from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_driver():
    """Setup Chrome driver with options."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("user-data-dir=/home/user/.config/google-chrome/ScriptProfile")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--disable-default-apps")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def check_text_present(driver, texts):
    """Check if any of the given texts are present on the page."""
    for text in texts:
        if driver.find_elements(By.XPATH, f"//*[contains(text(), '{text}')]"):
            print(f"Tekst {text} fundet!")
            return True
    return False

def click_element(driver, selector):
    """Wait for an element to be clickable and click it."""
    div = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
    )
    div.click()

def main():
    url = "https://www.lebara.dk/da/cart/mobile-number-from-another-operator-choice.html"
    texts_to_search = ['1234', '5678', '9012', '3456']
    driver = setup_driver()

    try:
        while True:
            driver.get(url)
            try:
                click_element(driver, "div[data-testid='radio-card-new_number']")
                time.sleep(2)  # Tilpas denne sleep tid efter behov

                if check_text_present(driver, texts_to_search):
                    break
                else:
                    print("Tekster ikke fundet, genindlæser siden...")
            except Exception as e:
                print(f"En fejl opstod: {e}, prøver igen...")

        print("Script afsluttet. Du kan nu interagere med browseren.")
        input("Tryk Enter for at afslutte og lukke browseren...")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
