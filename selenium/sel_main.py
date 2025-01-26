# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Initialize the WebDriver (make sure to specify the path to your driver if needed)
# driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.
# driver.get("https://tools.sars.gov.za/tradestatsportal/data_download.aspx")


# # Wait for the page to load
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_rdbImports")))

# # Select the 'Imports' radio button
# imports_radio = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_rdbImports")
# imports_radio.click()

# # Select the 'Countries' radio button (if not already checked)
# countries_radio = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_rdbCountries")
# # if not countries_radio.is_selected():
# countries_radio.click()

# # Check the 'Select all' checkbox for countries
# select_all_countries = driver.find_element(By.NAME, "ctl00_ContentPlaceHolder1_ddlCountries0_sll")
# if not select_all_countries.is_selected():
#     select_all_countries.click()

# # Check specific chapters (you can repeat this for other checkboxes)
# chapter_checkbox = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlChapters_26")
# if not chapter_checkbox.is_selected():
#     chapter_checkbox.click()

# # Check 'Select all' checkbox for tariffs
# select_all_tariffs = driver.find_element(By.NAME, "ctl00_ContentPlaceHolder1_ddlTariffs_sll")
# if not select_all_tariffs.is_selected():
#     select_all_tariffs.click()

# # Check year 2024 checkbox
# year_2024_checkbox = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlYears_14")
# if not year_2024_checkbox.is_selected():
#     year_2024_checkbox.click()

# # Check August checkbox (example)
# august_checkbox = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlMonths_7")
# if not august_checkbox.is_selected():
#     august_checkbox.click()

# # **NEW**: Check the 'Select All' checkbox at the bottom
# select_all_checkbox = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_chkAll")
# if not select_all_checkbox.is_selected():
#     select_all_checkbox.click()


# download_button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnDownload")
# download_button.click()

# driver.quit()
# ----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from selenium.common.exceptions import StaleElementReferenceException

# # Function to safely click an element
# def safe_click(driver, by, value):
#     try:
#         element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))
#         element.click()
#     # except StaleElementReferenceException:
#     #     print("StaleElementReferenceException caught. Retrying...")
#     #     time.sleep(5)  # Optional: wait a moment before retrying
#     #     safe_click(driver, by, value)  # Retry clicking
#     # Inside safe_click function
#     except StaleElementReferenceException:
#         print("StaleElementReferenceException caught. Retrying...")
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))  # Wait for element to be present again
#         safe_click(driver, by, value)  # Retry clicking

# # Initialize the WebDriver (make sure to specify the path to your driver if needed)
# driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.
# driver.get("https://tools.sars.gov.za/tradestatsportal/data_download.aspx")
# #--------------
# # Wait for the page to load and select 'Imports' radio button
# safe_click(driver, By.ID, "ctl00_ContentPlaceHolder1_rdbImports")

# # Select 'Countries' radio button (if not already checked)
# countries_radio = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_rdbCountries")
# if not countries_radio.is_selected():
#     safe_click(driver, By.ID, "ctl00_ContentPlaceHolder1_rdbCountries")
# #---------------------
# # **NEW**: Click to open the country dropdown menu
# country_dropdown = driver.find_element(By.ID, "caption0")  # Adjust if necessary to target the correct element
# safe_click(driver, By.ID, "caption0")  # This should open the dropdown

# # Wait for the dropdown options to be visible (you may need to adjust this based on your specific case)
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "dd_chk_drop")))

# # Check 'Select all' checkbox for countries in the dropdown
# select_all_countries = driver.find_element(By.NAME, "ctl00_ContentPlaceHolder1_ddlCountries0_sll")
# if not select_all_countries.is_selected():
#     safe_click(driver, By.NAME, "ctl00_ContentPlaceHolder1_ddlCountries0_sll")
# safe_click(driver, By.ID, "caption0") 
# #--------------
# # Check specific chapters

# # chapter_checkbox = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlChapters_26")
# # if not chapter_checkbox.is_selected():
# #     safe_click(driver, By.ID, "ctl00_ContentPlaceHolder1_ddlChapters_26")

# # Click to open the chapters dropdown menu
# # chapters_dropdown = driver.find_element(By.ID, "caption1")
# country_dropdown = driver.find_element(By.ID, "caption1")
# safe_click(driver, By.ID, "caption1")  # Opens the chapters dropdown

# # Wait for the chapters options to be visible
# WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "dd_chk_drop")))
# # Scroll down to make Chapter 27 visible and select it
# # ---------------------chapter_27_checkbox = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlChapters_26")  
# # ------------------------driver.execute_script("arguments[0].scrollIntoView(true);", chapter_27_checkbox)  # Scrolls to Chapter 27 checkbox

# #-------------if not chapter_27_checkbox.is_selected():
#     # -------------safe_click(driver, By.ID, "ctl00_ContentPlaceHolder1_ddlChapters_26")  # Click on Chapter 27 checkbox

# chapter_27_checkbox = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlChapters_0")
# driver.execute_script("arguments[0].scrollIntoView(true);", chapter_27_checkbox)  # Scrolls to Chapter 27 checkbox
# if not chapter_27_checkbox.is_selected():
#     safe_click(driver, By.ID, "ctl00_ContentPlaceHolder1_ddlChapters_0")  # Click on Chapter 27 checkbox



# # # Check Chapter 27 checkbox (adjust ID or name if necessary)
# # chapter_27_checkbox = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlChapters_26")  # Ensure this ID corresponds to Chapter 27
# # if not chapter_27_checkbox.is_selected():
# #     safe_click(driver, By.ID, "ctl00_ContentPlaceHolder1_ddlChapters_26")

# # safe_click(driver, By.ID, "caption1")  # Closes the chapters dropdown

# #----------
# safe_click(driver, By.ID, "caption2")
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "dd_chk_drop")))

# # Check 'Select all' checkbox for tariffs
# select_all_tariffs = driver.find_element(By.NAME, "ctl00_ContentPlaceHolder1_ddlTariffs_sll")
# if not select_all_tariffs.is_selected():
#     safe_click(driver, By.NAME, "ctl00_ContentPlaceHolder1_ddlTariffs_sll")

# # Check year 2024 checkbox
# year_2024_checkbox = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlYears_14")
# if not year_2024_checkbox.is_selected():
#     safe_click(driver, By.ID, "ctl00_ContentPlaceHolder1_ddlYears_14")

# # Check August checkbox (example)
# august_checkbox = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlMonths_7")
# if not august_checkbox.is_selected():
#     safe_click(driver, By.ID, "ctl00_ContentPlaceHolder1_ddlMonths_7")

# # Check 'Select All' checkbox at the bottom
# select_all_checkbox = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_chkAll")
# if not select_all_checkbox.is_selected():
#     safe_click(driver, By.ID, "ctl00_ContentPlaceHolder1_chkAll")

# # Click the download button
# safe_click(driver, By.ID, "ctl00_ContentPlaceHolder1_btnDownload")

# # Cleanup: Close the browser after your operations are complete
# driver.quit()

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

# Function to safely click an element
def safe_click(driver, by, value):
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))
        element.click()
    except StaleElementReferenceException:
        print("StaleElementReferenceException caught. Retrying...")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))  # Wait for element to be present again
        safe_click(driver, by, value)  # Retry clicking

# Initialize the WebDriver (make sure to specify the path to your driver if needed)
driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.
driver.get("https://tools.sars.gov.za/tradestatsportal/data_download.aspx")

# Wait for the page to load and select 'Imports' radio button
safe_click(driver, By.ID, "ctl00_ContentPlaceHolder1_rdbImports")

# Select 'Countries' radio button (if not already checked)
countries_radio = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_rdbCountries")
if not countries_radio.is_selected():
    safe_click(driver, By.ID, "ctl00_ContentPlaceHolder1_rdbCountries")

# Click to open the country dropdown menu
country_dropdown = driver.find_element(By.ID, "caption0")
safe_click(driver, By.ID, "caption0")  # Open the dropdown

# Wait for the dropdown options to be visible
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "dd_chk_drop")))

# Check 'Select all' checkbox for countries in the dropdown
select_all_countries = driver.find_element(By.NAME, "ctl00_ContentPlaceHolder1_ddlCountries0_sll")
if not select_all_countries.is_selected():
    safe_click(driver, By.NAME, "ctl00_ContentPlaceHolder1_ddlCountries0_sll")
safe_click(driver, By.ID, "caption0")  # Close the dropdown


# ________TRY TO SELECT CHAPTERS____________________

# Click t
# __________________________________________________
# Click to open the chapters dropdown menu
safe_click(driver, By.ID, "caption1")  # Opens the chapters dropdown

# Wait for the chapters dropdown container to be visible using its ID
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_ddlChapters_dv")))

# Locate the checkbox for "04 - Dairy produce" using its ID and click it
dairy_produce_checkbox = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlChapters_3")

# If it's not already selected, click it
if not dairy_produce_checkbox.is_selected():
    safe_click(driver, By.ID, "ctl00_ContentPlaceHolder1_ddlChapters_3")

# Close the chapters dropdown
safe_click(driver, By.ID, "caption1")


# # Click to open the chapters dropdown menu
# safe_click(driver, By.ID, "caption1")  # Opens the chapters dropdown

# # Wait for the chapters options to be visible
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "dd_chk_drop")))

# # Scroll down to make Chapter 27 visible and select it
# chapter_27_checkbox = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_ddlChapters_0"))
# )
# driver.execute_script("arguments[0].scrollIntoView(true);", chapter_27_checkbox)  # Scroll to Chapter 27 checkbox
# if not chapter_27_checkbox.is_selected():
#     safe_click(driver, By.ID, "ctl00_ContentPlaceHolder1_ddlChapters_0")

# # Close the chapters dropdown
# safe_click(driver, By.ID, "caption1")

# Click to open the tariffs dropdown menu
tarrifs_dropdown = driver.find_element(By.ID, "caption2")
safe_click(driver, By.ID, "caption2")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "dd_chk_drop")))

# Check 'Select all' checkbox for tariffs
select_all_tariffs = driver.find_element(By.NAME, "ctl00_ContentPlaceHolder1_ddlTariffs_sll")
if not select_all_tariffs.is_selected():
    safe_click(driver, By.NAME, "ctl00_ContentPlaceHolder1_ddlTariffs_sll")

# Check year 2024 checkbox
year_2024_checkbox = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlYears_14")
if not year_2024_checkbox.is_selected():
    safe_click(driver, By.ID, "ctl00_ContentPlaceHolder1_ddlYears_14")

# Check August checkbox
august_checkbox = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlMonths_7")
if not august_checkbox.is_selected():
    safe_click(driver, By.ID, "ctl00_ContentPlaceHolder1_ddlMonths_7")

# Check 'Select All' checkbox at the bottom
select_all_checkbox = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_chkAll")
if not select_all_checkbox.is_selected():
    safe_click(driver, By.ID, "ctl00_ContentPlaceHolder1_chkAll")

# Click the download button
safe_click(driver, By.ID, "ctl00_ContentPlaceHolder1_btnDownload")

# Cleanup: Close the browser after your operations are complete
driver.quit()
