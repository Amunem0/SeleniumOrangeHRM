from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Step 1: Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# Step 2: Wait for elements to be present
wait = WebDriverWait(driver, 10)

try:
    # Step 3: Login
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    username_field.send_keys("Admin")
    password_field.send_keys("admin123")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Step 4: Wait for Dashboard
    wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
    print("Login successful!")

    # Step 5: Navigate to Leave Assignment
    leave_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Leave']")))
    leave_menu.click()
    assign_leave_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Assign Leave']")))
    assign_leave_menu.click()

    # Step 6: Wait for Assign Leave form
    wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Assign Leave']")))
    print("Assign Leave form loaded.")

    # Step 7: Enter Employee Name
    employee_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type for hints...']")))
    employee_field.send_keys("Ravi M B")
    time.sleep(2)
    employee_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Ravi M B']")))
    employee_option.click()

    # Step 8: Select Leave Type
    leave_type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='oxd-select-text-input']")))
    leave_type_dropdown.click()
    leave_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='CAN - Personal']")))
    leave_option.click()

    # Step 9: Select From Date (3 March 2025)
    from_date_icon = driver.find_element(By.XPATH, "(//i[contains(@class, 'oxd-icon bi-calendar')])[1]")
    from_date_icon.click()
    from_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='oxd-calendar-date' and text()='3']")))
    from_date.click()

    # Step 10: Select To Date (10 March 2025)
    to_date_icon = driver.find_element(By.XPATH, "(//i[contains(@class, 'oxd-icon bi-calendar')])[2]")
    to_date_icon.click()
    to_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='oxd-calendar-date' and text()='10']")))
    to_date.click()
    print("Valid date selection: From 3 March 2025 to 10 March 2025.")

    # Step 11: Select Partial Days and Choose "All Days"
    partial_days_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Partial Days']/following::div[contains(@class, 'oxd-select-text')]")))
    partial_days_dropdown.click()
    all_days_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='All Days']")))
    all_days_option.click()
    print("Selected 'All Days' in Partial Days.")

    # Step 12: Select Duration and Choose "Specify Time"
    duration_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Duration']/following::div[contains(@class, 'oxd-select-text')]")))
    duration_dropdown.click()
    specify_time_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Specify Time']")))
    specify_time_option.click()
    print("Selected 'Specify Time' for duration.")

    # Step 13: Fill From Time and To Time by clicking the clock button
    from_time_clock = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='From']/following-sibling::div//i[contains(@class, 'bi-clock')]")))
    from_time_clock.click()
    from_time_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='From']/following-sibling::div//input")))
    from_time_input.clear()
    from_time_input.send_keys("10:00 AM")

    to_time_clock = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='To']/following-sibling::div//i[contains(@class, 'bi-clock')]")))
    to_time_clock.click()
    to_time_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='To']/following-sibling::div//input")))
    to_time_input.clear()
    to_time_input.send_keys("06:00 PM")

    print("Time updated: From 10:00 AM to 06:00 PM")

    # Step 14: Enter Comments
    comments = driver.find_element(By.TAG_NAME, "textarea")
    comments.send_keys("Assigning leave for Ravi M B.")

    # Step 15: Submit Leave Assignment
    assign_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Assign ']")))
    assign_button.click()

    print("Leave assignment submitted successfully.")

except Exception as e:
    print("An error occurred:", e)

finally:
    time.sleep(10)
    driver.quit()
