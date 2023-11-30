# Webscraping Tennis Rankings

This Python script retrieves ATP tennis player rankings from the 
Ultimate Tennis Statistics website and displays the information based on user input.

Initially we tried using _requests_ and _BeautifulSoup_ libraries to parse the data from the tables, but after an initial trial, it was clear that te website is dynamic. Therefore, we switched to using _selenium_. 
One of the common issues that we came across is being able to extract the table date during the debugging process, but not when executing the script. This issue arises when selenium closes the driver before it is able to parse the html. In order to overcome this issue, we utilized the _time.sleep()_, _WebDriverWait_ and _expected_conditions_ modules. For example, part of the `tennis_rankings.py` script includes clicking on a drop down menu to change the number of display results. We found that the driver would often close right away after selecting the chosen number, not having enough time to extract the table on the webpage:

        `# After opening dropdown menu, clicks on chosen number of display results
        option_display = WebDriverWait(dropdown_menu, 10).until( 
            EC.element_to_be_clickable((By.LINK_TEXT, display_num))
        )
        option_display.click()`

        # Force sleep for 1 second to ensure driver does not close too quickly and cause player_rows = []
        time.sleep(1)
        player_rows = driver.find_elements_by_css_selector('tbody tr')


## Dependencies
- __selenium__

  `pip install selenium`

- __WebDriver__: make sure you have the Chrome WebDriver executable installed and available
  in your system path. Ensure that the version is compatible with you chrome browser. You can download the driver [here](https://chromedriver.chromium.org/downloads).

- other dependencies can be found in the __requirements.txt__ file

## Usage
1. Clone the repository or download the following scripts:
- `main.py`
- `tennis_rankings.py`
- `head_2_head.py`
- `logger.py`

2. Run the script in your cmd:
    `python main.py`
   
4. Follow the onscreen prompts. 
5. The script will fetch the data from the Ultimate Tennis Statistics website and display the results.

## Logging
The script logs relevant information and errors to a file named `tennis.log`

