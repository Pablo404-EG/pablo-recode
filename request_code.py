from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def request_code(phone_number, attempts):
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        for attempt in range(1, attempts + 1):
            print(f"Attempting to request code #{attempt} for number {phone_number}...")

            
            driver.get(f"https://web.whatsapp.com/send?phone={phone_number}")

            
            time.sleep(5)

            
            try:
                code_request_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Request code')]")
                code_request_button.click()
                print(f"Code requested successfully on attempt #{attempt}")
            except Exception as e:
                print(f"Error on attempt #{attempt}: {e}")
            
            
            time.sleep(1)
    
    except Exception as e:
        print(f"Critical error: {e}")
    
    finally:
        driver.quit()
        print("Session ended. Exiting tool.")

def main():
    print("WhatsApp Code Request Tool")
    country_code = input("Enter the country code (e.g., 1 for USA): ")
    phone_number = input(f"Enter the phone number without country code: +{country_code} ")
    full_number = f"{country_code}{phone_number}"
    attempts = int(input("How many times do you want to request the code? "))

    print(f"Starting code requests for number {full_number} for {attempts} times...")
    request_code(full_number, attempts)

if __name__ == "__main__":
    main()
