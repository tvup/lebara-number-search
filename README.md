### README

## Selenium Script for Automated Interaction with Chrome Browser

This Python script uses Selenium to automate the interaction with a webpage. Specifically, it reloads the page, clicks on a specific element, and searches for certain texts. If any of the texts are found, the script stops and allows the user to interact with the browser manually.

### Prerequisites

- Python 3.x
- Google Chrome
- ChromeDriver
- Selenium package

### Installation

1. **Install Python**:
   Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/).

2. **Install Selenium**:
   Install the Selenium package using pip:
   ```sh
   pip install selenium
   ```

3. **Download ChromeDriver**:
   Download ChromeDriver from the [official site](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in your PATH or in the same directory as your script.

### Usage

1. **Configure Chrome Profile**:
   - Open Google Chrome and create a new profile.
   - Configure the profile with your desired settings (e.g., select the default search engine).
   - Locate the profile directory. On Ubuntu, it should be something like:
     ```
     /home/<username>/.config/google-chrome/Profile X
     ```
   - Replace `<username>` with your actual username and `Profile X` with the profile you configured. In the script, it is set to `/home/tvup/.config/google-chrome/ScriptProfile`.

2. **Update the Script**:
   - Ensure the `user-data-dir` argument in `setup_driver()` points to your Chrome profile directory.
   - Update the `texts_to_search` list with the texts you are looking for.
   - Update the URL in the `main()` function to the target webpage.

3. **Run the Script**:
   Save the script as `script.py` and run it:
   ```sh
   python script.py
   ```

### Script Explanation

- **setup_driver()**:
  Configures and returns a Chrome WebDriver with specific options, including the use of a custom user profile.

- **check_text_present(driver, texts)**:
  Checks if any of the given texts are present on the page.

- **click_element(driver, selector)**:
  Waits for an element to be clickable and clicks on it.

- **main()**:
  The main function that orchestrates the page loading, clicking the element, and checking for texts.

### Notes

- Ensure all Chrome instances are closed before running the script to avoid profile conflicts.
- The script will keep running and reloading the page until it finds one of the specified texts.
- Once a text is found, the script will stop and allow user interaction. The browser will close when the user presses Enter in the terminal.
