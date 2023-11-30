from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tennis_logger import logger
from tabulate import tabulate


def head_2_head(player1, player2):
    driver = webdriver.Chrome()
    head2head_url = "https://www.ultimatetennisstatistics.com/headToHead"
    print("\nCharging page...")
    try:
        driver.get(head2head_url)
        logger.info(f"Successfully fetched URL: {head2head_url}")
    except Exception as e:
        logger.error(f"{e}: Failed to fetch URL: {head2head_url}")

    try:
        player1_input = driver.find_element(By.ID, "player1")
        player1_input.send_keys(player1)
        time.sleep(2)
        suggestion = driver.find_element(By.CLASS_NAME, "ui-menu-item-wrapper")
        suggestion.click()
        logger.info(f"Successfully fetched information on player 1: {player1}")
    except Exception as e:
        logger.error(f"{e}: Failed to fetch information on player 1: {player1}")
        print(f"Player '{player1}' does not exist")
        return

    try:
        player2_input = driver.find_element(By.ID, "player2")
        player2_input.send_keys(player2)
        time.sleep(2)
        suggestion = driver.find_element(By.CLASS_NAME, "ui-menu-item-wrapper")
        suggestion.click()
        logger.info(f"Successfully fetched information on player 2: {player2}")
    except Exception as e:
        logger.info(f"{e}: Failed to fetch information on player 2: {player2}")
        print(f"Player '{player2}' does not exist")
        return

    print_stats(driver)


def print_stats(driver):
    p1 = driver.find_element(By.CLASS_NAME, "text-left").text
    p2 = driver.find_element(By.CLASS_NAME, "text-right").text
    w1 = driver.find_element(By.CLASS_NAME, "progress-bar.progress-bar-perf-w").text
    w2 = driver.find_element(By.CLASS_NAME, "progress-bar.progress-bar-perf-l").text
    characteristics = driver.find_elements(By.CSS_SELECTOR, "tr")

    data = [["Wins", w1, w2]]

    for char in characteristics:
        if 'Age' in char.text:
            age1 = char.find_element(By.CLASS_NAME, "text-right").text
            age2 = char.find_element(By.CLASS_NAME, "text-left").text
            data.append(["Age", age1, age2])
        if "Country" in char.text:
            country1 = char.find_element(By.CLASS_NAME, "text-right").text
            country2 = char.find_element(By.CLASS_NAME, "text-left").text
            data.append(["Country", country1, country2])
        if "Height" in char.text:
            h1 = char.find_element(By.CLASS_NAME, "text-right").text
            h2 = char.find_element(By.CLASS_NAME, "text-left").text
            data.append(["Height", h1, h2])
        if "Weight" in char.text:
            w1 = char.find_element(By.CLASS_NAME, "text-right").text
            w2 = char.find_element(By.CLASS_NAME, "text-left").text
            data.append(["Weight", w1, w2])
        if "Plays" in char.text:
            hand1 = char.find_element(By.CLASS_NAME, "text-right").text
            hand2 = char.find_element(By.CLASS_NAME, "text-left").text
            data.append(["Plays", hand1, hand2])
        if "Titles" in char.text:
            t1 = char.find_element(By.CLASS_NAME, "text-right").text
            t2 = char.find_element(By.CLASS_NAME, "text-left").text
            data.append(["Titles", t1, t2])
        if "Grand Slams" in char.text:
            gs1 = char.find_element(By.CLASS_NAME, "text-right").text
            gs2 = char.find_element(By.CLASS_NAME, "text-left").text
            data.append(["Grand Slams", gs1, gs2])
        if "Best Season" in char.text:
            bs1 = char.find_element(By.CLASS_NAME, "text-right").text
            bs2 = char.find_element(By.CLASS_NAME, "text-left").text
            data.append(["Best Season", bs1, bs2])
        if "Best Rank" in char.text:
            br1 = char.find_element(By.CLASS_NAME, "text-right").text
            br2 = char.find_element(By.CLASS_NAME, "text-left").text
            data.append(["Best Rank", br1, br2])
        if "Prize Money" in char.text:
            pm1 = char.find_element(By.CLASS_NAME, "text-right").text
            pm2 = char.find_element(By.CLASS_NAME, "text-left").text
            data.append(["Prize Money", pm1, pm2])

    print("\n", tabulate(data, headers=["Characteristic", p1, p2], tablefmt="pretty"))


def menu():
    print("\n *** WELCOME TO HEAD 2 HEAD *** \n")
    player1_name = input("Please, enter Player 1 : ")
    player2_name = input("Please, enter Player 2 : ")
    head_2_head(player1_name, player2_name)


def main():
    menu()


if __name__ == "__main__":
    main()
