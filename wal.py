#!/usr/bin/env python3

import argparse
import os
import sys
import yaml

# Import web test suite
# docs: http://selenium-python.readthedocs.io/
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains

class Wal(object):
    def __init__(self):
        '''
        Set up wal. Use -h to see available commands.
        '''
        parser = argparse.ArgumentParser(description='wal - web' +
                                         'automation layer.\n' +
                                         'Simple web automation ' +
                                         'using yaml syntax.')
        parser.add_argument('input_files',
                            default=sys.stdin,
                            nargs='*')
        self.args = parser.parse_args()
        self.scripts = []
        for script_name in self.args.input_files:
            self.scripts.append({script_name: self.load_script(script_name)})
        self.select = None


    def load_script(self, script):
        commands = []
        line_num = 0
        with open(script, 'r') as stream:
            try:
                line_num += 1
                commands.append(yaml.load(stream))
            except yaml.YAMLError as exc:
                print(exc)

        return commands


    def print_scripts(self):
        for script in self.scripts:
            line_num = 0
            for script_name in script.keys():
                print('-'*80)
                print(script_name)
                print('-'*80)
            for commands in script.values():
                if len(commands) > 0:
                    for line in commands[0]:
                        line_num += 1
                        print(line_num, '|', line)


    def interpret(self, line):
        for key in line.keys():
            command = key
        for value in line.values():
            argument = value
        print(command, ':\t', argument)
        if command == 'set_window_size':
            self.driver.set_window_size('500','500')
        elif command == 'get':
            self.driver.get(argument[0])
            the_d = self.driver.get
            print(the_d)
            print('now at ', self.driver.current_url)
        elif command == 'save_screenshot':
            self.driver.save_screenshot(argument[0])

    def print_element(self):
        print('tag_name: ', self.select.tag_name)
        print('name: ', self.select.get_attribute('name'))
        print('id: ', self.select.get_attribute('id'))
        print('class: ', self.select.get_attribute('class'))
        print('selenium_id: ', self.select.id)


    def run(self):
        for script in self.scripts:
            line_num = 0
            for script_name in script.keys():
                print('-'*80)
                print(script_name)
                print('-'*80)
            try:
                for commands in script.values():
                    # set up drive
                    driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
                    # set default home page
                    driver.get('http://about:blank')
                    # set default screen size
                    driver.set_window_size(1366,768)
                    # if commands empty, continue
                    if len(commands) == 0:
                        break
                    # interpret commands
                    for line in commands[0]:
                        line_num += 1
                        print(line_num, '|', end='')
                        if type(line) is str:
                            command = key
                        if type(line) is dict:
                            for key in line.keys():
                                command = key
                            for value in line.values():
                                argument = value
                        # print command
                        print(' - ' + command + ':', end='')
                        # only print argument if it's a string
                        if type(argument) is str:
                            print('\t\'' + argument + '\'', end='')
                        print()  # print new line
                        # connect yaml commands to selenium driver commands
                        if command == 'set_window_size':
                            if type(argument) is list:
                                driver.set_window_size(int(argument[0]),
                                                       int(argument[1]))
                            if type(argument) is str:
                                seperator = argument.find('x')
                                width = argument[0:seperator]
                                height = argument[-(seperator - 1):]
                                driver.set_window_size(width, height)
                        elif command == 'foreach':
                            class_name = None
                            print_href = None
                            if type(argument) is list:
                                for arg in argument:
                                    line_num += 1
                                    key = list(arg.keys())[0]
                                    value = list(arg.values())[0]
                                    print(line_num, '|', end='')
                                    print('    - ' + key + ':\t' +
                                          '\'' + value + '\'')
                                    if key == 'class':
                                        self.select = driver.find_element_by_class_name(value)
                                        class_name = value
                                    if key == 'print_href':
                                        print_href = True
                                if type(class_name) is not None and print_href is True:
                                    elements = driver.find_elements_by_class_name(class_name)
                                    for element in elements:
                                        print(element.get_attribute('href'))
                        elif command == 'get':
                            if type(argument) is list:
                                argument = argument[0]
                            if type(argument) is str:
                                driver.get(argument)
                        elif command == 'save_screenshot':
                            if type(argument) is list:
                                argument = argument[0]
                            if type(argument) is str:
                                driver.save_screenshot(argument)
                        elif command == 'select':
                            if type(argument) is list:
                                argument = argument[0]
                            if type(argument) is str:
                                if argument[:1] == '#':
                                    self.select = driver.find_element_by_id(argument)
                                elif argument[:1] == '.':
                                    self.select = driver.find_element_by_class_name(argument)
                                else:
                                    self.select = driver.find_element_by_name(argument)
                        elif command == 'select_by_id':
                            if type(argument) is list:
                                argument = argument[0]
                            if type(argument) is str:
                                self.select = driver.find_element_by_id(argument)
                        elif command == 'select_by_class':
                            if type(argument) is list:
                                argument = argument[0]
                            if type(argument) is str:
                                self.select = driver.find_element_by_class_name(argument)
                        elif command == 'select_by_name':
                            if type(argument) is list:
                                argument = argument[0]
                            if type(argument) is str:
                                self.select = driver.find_element_by_name(argument)
                        elif command == 'select_by_value':
                            if type(argument) is list:
                                argument = argument[0]
                            if type(argument) is str:
                                self.select = driver.find_element_by_value(argument)
                        elif command == 'select_by_xpath':
                            if type(argument) is list:
                                argument = argument[0]
                            if type(argument) is str:
                                self.select = driver.find_element_by_xpath(argument)
                        elif command == 'select_by_tagname':
                            if type(argument) is list:
                                argument = argument[0]
                            if type(argument) is str:
                                self.select = driver.find_element_by_tagname(argument)
                        elif command == 'deselect':
                            if type(argument) is list:
                                argument = argument[0]
                            if type(argument) is str:
                                driver.dselect_all()
                        elif command == 'clear':
                            driver.clear()
                        # TODO: add support for special keys
                        elif command == 'send_keys':
                            if type(argument) is list:
                                for arg in argument:
                                    self.select.send_keys(argument)
                            if type(argument) is str:
                                self.select.send_keys(argument)
                        elif command == 'submit':
                            if type(argument) is None:
                                if type(self.select) is None:
                                    print('Error: submit: Nothing is selected.')
                                try:
                                    self.select.submit()
                                except NoSuchElementException as error:
                                    print(str(error))
                            if type(argument) is list:
                                argument = argument[0]
                            if type(argument) is str:
                                if argument[:1] == '#':
                                    self.select =driver.find_element_by_id(argument)
                                elif argument[:1] == '.':
                                    self.select =driver.find_element_by_class(argument)
                                else:
                                    self.select = driver.find_element_by_name(argument)
                                try:
                                    self.select.submit()
                                except NoSuchElementException as error:
                                    print(str(error))
                            try:
                                self.select.submit()
                            except NoSuchElementException as error:
                                print(str(error))
                        elif (command == 'forward' or
                              command == 'forwards'):
                            driver.forward()
                        elif (command == 'back' or
                              command == 'backward' or
                              command == 'backwards'):
                            driver.back()
                        elif (command == 'print_url' or
                              command == 'current_url'):
                            print(driver.current_url)
                        elif command == 'click':
                            if type(argument) is None:
                                self.select.click()
                            if type(argument) is list:
                                argument = argument[0]
                            if type(argument) is str:
                                if argument[:1] == '#':
                                    self.select =driver.find_element_by_id(argument)
                                elif argument[:1] == '.':
                                    self.select =driver.find_element_by_class(argument)
                                else:
                                    self.select = driver.find_element_by_name(argument)
                                self.select.click()

            except WebDriverException as error:
                print("Web Driver Error:" + str(error))
            finally:
                driver.quit()

        
def main():
    wal = Wal()
    wal.run()


if __name__ == "__main__":
    main()
