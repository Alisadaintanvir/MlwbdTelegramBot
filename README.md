# Automated Movie Download Telegram Bot from MLWBD using Selenium

This repository contains a Python script that automates the process of downloading movies from the MLWBD website using the Selenium WebDriver. The script interacts with the website's UI elements to navigate through the download process and provides the final download link for the specified movie.

## Prerequisites:

- Python 3.x
- Selenium library
- Google Chrome browser
- ChromeDriver (compatible with your Chrome browser version)

## Instructions:

1. Install Selenium library:

   `pip install selenium`

3. Download and install the appropriate ChromeDriver version:
- Visit the ChromeDriver download page and download the version compatible with your Chrome browser.
- 
3. Place the downloaded ChromeDriver executable in the same directory as the script.

4. Run the script:

- Open a terminal and navigate to the directory containing the script.
- Run the script using the command:

   `python main.py`

5. Enter the movie link from MLWBD when prompted.

6. The script will automatically navigate through the download process on MLWBD and provide you with the final download page link for the specified movie.

## Explanation of the Script:

1. Import necessary modules and libraries.
2. Get the movie URL input from the user and extract the movie title from the URL.
3. Set up headless Chrome options to run the browser in the background.
4. Initialize the Chrome WebDriver.
5. Access the specified URL and store the initial window handle.
6. Find and store the ID of the movie download form.
7. Execute a JavaScript script to submit the download form and switch to the new window handle.
8. Find and click on various download buttons using XPath and explicit waits.
9. Print the final download page link for the user.
10. Close the WebDriver and exit.

## Note:

- This script is provided for educational purposes only and may not be compatible with future changes to the MLWBD website structure. Use at your own discretion.
- Automated scraping and downloading from websites may violate their terms of service. Always make sure to comply with website policies and legal regulations.
- This script relies on specific UI element paths (XPath) on the MLWBD website. If the website's structure changes, the script may break and require updates.

Feel free to fork, modify, and improve this script according to your needs.
