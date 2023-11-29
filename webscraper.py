import requests
import logging
import json
from bs4 import BeautifulSoup
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

with open('conf.json', 'r') as config_file:
    config = json.load(config_file)

player_ranking_url = config['player_ranking_url']
second_url = config['second_url']

logging.basicConfig(
    filename='tennis.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def get_players_info(driver, display_num):
    """ """
    try:
        # Clicking button responsible for number of display results.
        button = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#rankingsTable-header > div > div > div.actions.btn-group > div:nth-child(2) > button"))
        )
        button.click()

        # Locating the dropdown menu options
        dropdown_menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#rankingsTable-header > div > div > div.actions.btn-group > div.dropdown.btn-group.open > ul"))
        )

        # Selecting number of display results as 100
        option_display = WebDriverWait(dropdown_menu, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, display_num))
        )
        option_display.click()

        time.sleep(1)
        player_rows = driver.find_elements_by_css_selector('tbody tr')

    except Exception:
        driver.quit()
        return []


    if len(player_rows) == 100:
        logging.info(f"Successfully fetched 100 rows from table.")
    else:
        logging.error(f"Failed to fetch 100 rows, only retrieved {len(player_rows)} rows.")

    players_info = []
    for row in player_rows:
        try:
            cells = row.find_elements_by_tag_name('td')
            row_data = {
                'ranking': cells[0].text,
                'best rank': cells[1].text,
                'country': cells[2].text,
                'name': cells[3].text,
                '+/- position': cells[4].text,
                '+/- points': cells[5].text
            }
            players_info.append(row_data)
            logging.info(f"Successfully extracted information on player {cells[3].text}.")
        except Exception:
            logging.info(f"Failed to extract information on player.")

    return players_info


def main():
    driver = webdriver.Chrome()
    try:
        driver.get(player_ranking_url)
        logging.info(f"Successfully fetched URL: {player_ranking_url}")
    except Exception as e:
        logging.error(f"Failed to fetch URL: {player_ranking_url}")
        driver.quit()

    num = '50'
    players = get_players_info(driver, num)
    for player in players:
        print(f"Ranking: {player['ranking']}, Player name: {player['name']}, Country: {player['country']}, "
              f"Best Rank: {player['best rank']}, Position Gains/Losses: {player['+/- position']}, "
              f"Points Gains/Losses: {player['+/- points']}")
    driver.quit()

if __name__ == '__main__':
    main()