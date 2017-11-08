#!/usr/bin/env python3
'''Web Automation Framework'''

import os

# Import web test suite
# docs: http://selenium-python.readthedocs.io/
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.webdriver.common.action_chains import ActionChains

def automate(driver):
    '''Examples of using Selenium + PhantomJs'''
    # Set window size.
    driver.set_window_size(1024, 768)
    # Get web page.
    driver.get('http://xkcd.com/')
    # Save screen shot.
    driver.save_screenshot('screen.png')
    # Get current element
    element = driver.switch_to.active_element
    # Press Return
    element.send_keys(Keys.RETURN)
    # Output to user that the screenshot was made
    print(driver.title)


def main():
    '''Put everything in a try/except/finally to ensure quit() is called.'''
    # Set up the PhantomJS web driver.
    thewebdriver = webdriver.PhantomJS(service_log_path=os.path.devnull)
    try:
        automate(thewebdriver)
    except exceptions.WebDriverException as error:
        print("Web Driver Error:" + error)
    finally:
        # This part is important
        # If quit() isn't called, you'll have processes
        # running around called: phantomjs
        thewebdriver.quit()


if __name__ == "__main__":
    main()
