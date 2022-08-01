from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import os
import re
import argparse
import sys
from decouple import config

def options() -> dict:

    '''
    Function to define arguments.

    Parameters
    ----------
    None

    Returns
    -------
    arg:dict Dict of arguments
    '''

    option = argparse.ArgumentParser()
    option.add_argument('-u', '--url', dest='url', help='url')
    option.add_argument('-f', '--file', dest='file', help='file with url list in')
    arg = vars(option.parse_args())
    
    return arg


class Screenshot():

    '''
    Class to take screenshots of webpages.
    Uses selenium and a headless firefox instance.
    Stores the png file in the screenshots directory
    '''

    def __init__(self, url:str) -> None:

        '''
        init function.

        Parameters
        ----------
        url:str string of url

        '''
        
        self.url = url
        self.png()
        self.filepaths()
        self.screenshot()
            
    def png(self) -> None:
        
        '''
        Function to name png file
        '''
        png_file_strip = re.sub(r'htt.*//', '', self.url)
        png_stip = re.sub(r'\n|\s', '', png_file_strip)
        self.png_file = re.sub(r'\.','_', png_stip)


    def filepaths(self) -> None:
        
        '''
        Function to define file paths for driver, screenshot directory and log file
        '''
        
        self.geckodriver = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'drivers/geckodriver')
        screen_shot_path = config('screenshots')
        self.png_path = f'{screen_shot_path}/{self.png_file}.png'
        self.log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')


    def screenshot(self) -> None:

        '''
        Function to open url in headlesss browser and take screenshot
        '''
        
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--headless")
        service = Service(self.geckodriver, log_path=f'{self.log_path}/geko.log')
        driver = webdriver.Firefox(service=service, options=firefox_options)
        driver.get(self.url)
        driver.save_screenshot(self.png_path)
        driver.quit()
        
if __name__ == '__main__':
    args = options()

    if args['file'] != None:
        with open(args['file']) as file:
            for line in file:
                Screenshot(line)
        sys.exit(0)
    
    Screenshot(args['url'])