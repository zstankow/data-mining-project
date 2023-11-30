# Webscraping Tennis Rankings

This Python script retrieves ATP tennis player rankings from the 
Ultimate Tennis Statistics website and displays the information based on user input.

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
