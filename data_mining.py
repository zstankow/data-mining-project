from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

NUMBER_OF_PLAYERS = 20


def get_players_info(driver):
    player_rows = driver.find_elements(By.CSS_SELECTOR, 'tbody tr')
    players_info = []
    for row in player_rows:
        player_info = {'Name': row.find_element(By.CLASS_NAME, 'player-cell-wrapper').text,
                       'Country': row.find_element(By.CSS_SELECTOR, 'td.country-cell.border-right-dash-1 img').get_attribute('alt'),
                       'Age': int(
                           row.find_element(By.CSS_SELECTOR, 'td.age-cell.border-left-dash-1.border-right-4').text),
                       'ranking': int(
                           row.find_element(By.CSS_SELECTOR, "td.rank-cell.border-left-4.border-right-dash-1").text),
                       'Points': row.find_element(By.CSS_SELECTOR, "td.points-cell.border-right-dash-1").text,
                       '+/- Points': row.find_element(By.CSS_SELECTOR, "td.points-move-cell.border-right-dash-1").text
                       }

        # Extracting data for each player

        # Append player's information to the list
        players_info.append(player_info)
    return players_info


def get_win_loss_stats(driver):
    win_loss_stats = driver.find_elements(By.CLASS_NAME, 'mega-table')
    win_loss_info = []
    for stat in win_loss_stats:
        info = {'Name': stat.find_element(By.CLASS_NAME, "player-cell").text,
                'YTD Index': stat.find_element(By.CLASS_NAME, "fifty-two-week-index-cell").text,
                'YTD Titles': stat.find_element(By.CLASS_NAME, "fifty-two-week-titles-cell").text,
                'YTD Win/Loss': stat.find_element(By.CLASS_NAME, "fifty-two-week-win-loss-cell").text
                }

        win_loss_info.append(info)
    return win_loss_info


def main():
    driver = webdriver.Chrome()

    # First webpage
    # driver.get("https://www.atptour.com/en/rankings/singles")
    # for player in get_players_info(driver):
    #     print(player)

    # Second webpage
    driver.get("https://www.ultimatetennisstatistics.com/rankingsTable")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#winLossTableList > div > table'))
            )
    except:
        driver.quit()
    for win_lost_stat in get_win_loss_stats(driver):
        print(win_lost_stat)
    driver.quit()


if __name__ == '__main__':
    main()
