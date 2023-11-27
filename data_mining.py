from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

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


def main():
    driver = webdriver.Chrome()
    driver.get("https://www.atptour.com/en/rankings/singles")
    for player in get_players_info(driver):
        print(player)
    driver.quit()


if __name__ == '__main__':
    main()
