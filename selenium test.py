from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def head_2_head(player1, player2):
    driver = webdriver.Chrome()
    driver.get("https://www.ultimatetennisstatistics.com/headToHead")
    player1_input = driver.find_element(By.ID, "player1")
    player1_input.send_keys(player1)
    time.sleep(1)
    suggestion = driver.find_element(By.CLASS_NAME, "ui-menu-item-wrapper")
    suggestion.click()

    player2_input = driver.find_element(By.ID, "player2")
    player2_input.send_keys(player2)
    time.sleep(1)
    suggestion = driver.find_element(By.CLASS_NAME, "ui-menu-item-wrapper")
    suggestion.click()
    time.sleep(1)
    print_stats(driver)


def print_stats(driver):
    matches = driver.find_elements(By.NAME, "Show H2H matches")
    print(matches)


def menu():
    print("\n *** WELCOME TO HEAD 2 HEAD *** \n")
    player1_name = input("Please, enter Player 1 : ")
    player2_name = input("Please, enter Player 2 : ")
    head_2_head(player1_name, player2_name)


def main():
    menu()


if __name__ == "__main__":
    main()
