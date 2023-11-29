from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.ultimatetennisstatistics.com/headToHead?tab=profiles&playerId1=4920&playerId2=3819")
p1 = driver.find_element(By.CLASS_NAME, "text-left")
print(p1.text)