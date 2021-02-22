import os
from pathlib import Path
class ReactCli:

    def __init__(self):
        """The constructor of the ReactCli class."""
        # Initializing our (empty) blockchain list
        self.type = ''


    def capitalize_each_word(self, original_str):
        result = ''
        # Split the string and get all words in a list
        list_of_words = original_str.split()
        # Iterate over all elements in list
        for elem in list_of_words:
            # capitalize first letter of each word and add to a string
            if len(result) > 0:
                result = result + " " + elem.strip().capitalize()
            else:
                result = elem.capitalize()
        # If result is still empty then return original string else returned capitalized.
        if not result:
            return original_str.replace(" ", "")
        else:
            return result.replace(" ", "")


    def create_component(self, file_name, styleSheet = False):
        if os.path.exists(file_name):
            print('Folder already exists')
        else:
            Path(file_name).mkdir(parents=True, exist_ok=True)
            try:
                with open('{}/{}.{}'.format(file_name, file_name, self.type), mode='w') as f:
                    f.write('import React from "react";')
                    f.write('\n')
                    if styleSheet:
                        f.write('import useStyles from "./{}.styles";'.format(file_name))
                    f.write('\n')
                    f.write('\n')
                    f.write('const %s = () => {' % (file_name))
                    f.write('\n')
                    f.write('const classes = useStyles();')
                    f.write('\n')
                    f.write('return (')
                    f.write('\n')
                    f.write('<div></div>')
                    f.write('\n')
                    f.write(')')
                    f.write('\n')
                    f.write('}')
                    f.write('\n')
                    f.write('\n')
                    f.write('export default {};'.format(file_name))

                    f.close()
            except IOError:
                print('Saving failed {} component file!'.format(file_name))
            if styleSheet:
                try:
                    with open('{}/{}.styles.{}'.format(file_name, file_name, self.type), mode='w') as f:
                        f.write('import { makeStyles } from "@material-ui/core";')
                        f.write('\n')
                        f.write('const useStyles = makeStyles((theme) => ({}));')
                        f.write('\n')
                        f.write('export default useStyles;')    
                        f.close()
                except IOError:
                     print('Saving failed {} stylesheet!'.format(file_name))

    
    def create_component_with_container(self, file_name, styleSheet = False):
        if os.path.exists(file_name):
            print('Folder already exists')
        else:
            Path(file_name).mkdir(parents=True, exist_ok=True)
            try:
                with open('{}/{}.{}'.format(file_name, file_name, self.type), mode='w') as f:
                    f.write('import React from "react";')
                    f.write('\n')
                    if styleSheet:
                        f.write('import useStyles from "./{}.styles";'.format(file_name))
                    f.write('\n')
                    f.write('\n')
                    f.write('const %s = () => {' % (file_name))
                    f.write('\n')
                    f.write('const classes = useStyles();')
                    f.write('\n')
                    f.write('return (')
                    f.write('\n')
                    f.write('<div></div>')
                    f.write('\n')
                    f.write(')')
                    f.write('\n')
                    f.write('}')
                    f.write('\n')
                    f.write('\n')
                    f.write('export default {};'.format(file_name))

                    f.close()
            except IOError:
                print('Saving failed {} component file!'.format(file_name))

            try:
                with open('{}/{}Container.{}'.format(file_name, file_name, self.type), mode='w') as f:
                    f.write('import React from "react";')
                    f.write('\n')
                    if styleSheet:
                        f.write('import useStyles from "./{}.styles";'.format(file_name))
                    f.write('\n')
                    f.write('import {} from "./{}";'.format(file_name, file_name))
                    f.write('\n')
                    f.write('const %sContainer = () => {' % (file_name))
                    f.write('\n')
                    f.write('const classes = useStyles();')
                    f.write('\n')
                    f.write('return (')
                    f.write('\n')
                    f.write('<{}></{}>'.format(file_name, file_name))
                    f.write('\n')
                    f.write(')')
                    f.write('\n')
                    f.write('}')
                    f.write('\n')
                    f.write('\n')
                    f.write('export default {}Container;'.format(file_name))

                    f.close()
            except IOError:
                print('Saving failed {} container file!'.format(file_name))
            if styleSheet:
                try:
                    with open('{}/{}.styles.{}'.format(file_name, file_name, self.type), mode='w') as f:
                        f.write('import { makeStyles } from "@material-ui/core";')
                        f.write('\n')
                        f.write('const useStyles = makeStyles((theme) => ({}));')
                        f.write('\n')
                        f.write('export default useStyles;')    
                        f.close()
                except IOError:
                     print('Saving failed {} stylesheet!'.format(file_name))


    def get_user_choice(self):
        """Prompts the user for its choice and return it."""
        user_input = input('Your choice: ')
        return user_input

    def js_or_ts(self):
        """Prompts the user for its choice and return it."""
        user_input = input('Do you want JS or TS: ')
        return user_input

    def listen_for_input(self):
        """Starts the node and waits for user input."""
        waiting_for_input = True

        # A while loop for the user input interface
        # It's a loop that exits once waiting_for_input becomes False or when break is called
        while waiting_for_input:
            print('Please choose')
            print('1: Component with stylesheet')
            print('2: Component without stylesheet')
            print('3: Component with container and stylesheet')
            print('q: Quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                folder_name = input('Please choose component name: ')
                self.create_component(self.capitalize_each_word(folder_name), True)
            if user_choice == '2':
                folder_name = input('Please choose component name: ')
                self.create_component(self.capitalize_each_word(folder_name))
            if user_choice == '3':
                folder_name = input('Please choose component name: ')
                self.create_component_with_container(self.capitalize_each_word(folder_name), True)
            elif user_choice == 'q':
                # This will lead to the loop to exist because it's running condition becomes False
                waiting_for_input = False
            else:
                print('Input was invalid, please pick a value from the list!')
        else:
            print('User left!')

        print('Done!')

    def listen_for_type(self):
        waiting_for_decision = True

         
        while waiting_for_decision:
            print('please choose JS or TS')
            print('1: JS')
            print('2: TS')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                self.type = 'js'
                self.listen_for_input()
            if user_choice == '2':
                self.type = 'ts'
                self.listen_for_input()
            else:
                print('Input was invalid, please pick a value from the list!')



if __name__ == '__main__':
    ReactCli = ReactCli()
    # ReactCli.listen_for_input()
    ReactCli.listen_for_type()