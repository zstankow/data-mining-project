from tennis_logger import logger
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



#
# logging.basicConfig(
#     filename='tennis.log',
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S'
# )


def get_players_info(driver, display_num):
    try:
        # Clicking button responsible for number of display results.
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 "#rankingsTable-header > div > div > div.actions.btn-group > div:nth-child(2) > button"))
        )
        button.click()

        # Locating the dropdown menu options
        dropdown_menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#rankingsTable-header > div > div > "
                                                             "div.actions.btn-group > div.dropdown.btn-group.open "
                                                             "> ul"))
        )

        # Selecting number of display results as 100
        option_display = WebDriverWait(dropdown_menu, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, display_num))
        )
        option_display.click()

        # Extracts table
        time.sleep(1)
        player_rows = driver.find_elements_by_css_selector('tbody tr')
        logger.info(f"Successfully fetched {display_num} rows from table.")

    except Exception as e:
        logger.error(f"{e}: Failed to fetch {display_num} rows.")
        driver.quit()
        return []
    return get_table(player_rows)


def get_table(player_rows):
    players_info = []
    for row in player_rows:
        try:
            cells = row.find_elements_by_tag_name('td')
            row_data = {
                'ranking': cells[0].text.split(" ")[0],
                'best rank': cells[1].text,
                'country': cells[2].text,
                'name': cells[3].text,
                '+/- position': cells[4].text,
                '+/- points': cells[5].text
            }
            players_info.append(row_data)
            logger.info(f"Successfully extracted information on ranked player number "
                        f"{row_data['ranking']}, player {row_data['name']}.")
        except Exception as e:
            logger.info(f"{e}: Failed to extract information on player.")

    return players_info


def verify_input(num):
    while True:
        if num not in ['20', '50', '100']:
            print("Sorry, that is not a valid input.")
            num = input("Please select the number of top tennis players' rankings you would "
                        "like to display: 20, 50, or 100: ")
        else:
            print("Just a moment...\n")
            return num


def print_ranking(players_info):
    for player in players_info:
        print(f"{player['ranking']}. {player['name']}, Country: {player['country']}, "
              f"Best Rank: {player['best rank']}, Position Gains/Losses: {player['+/- position']}, "
              f"Points Gains/Losses: {player['+/- points']}")


def menu():
    print("\n *** ATP RANKINGS *** \n")
    num_display = verify_input(input("Please select the number of top tennis players' rankings you would "
                                     "like to display: 20, 50, or 100: "))
    return num_display


def main():
    display = menu()
    driver = webdriver.Chrome()
    player_ranking_url = "https://www.ultimatetennisstatistics.com/rankingsTable"
    try:
        driver.get(player_ranking_url)
        logger.info(f"Successfully fetched URL: {player_ranking_url}")
    except Exception as e:
        logger.error(f"{e}: Failed to fetch URL: {player_ranking_url}")
        driver.quit()

    print_ranking(get_players_info(driver, display))
    driver.quit()


if __name__ == '__main__':
    main()
