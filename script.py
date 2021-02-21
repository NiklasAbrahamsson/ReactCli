import os
from pathlib import Path
class ReactCli:

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


    def ensure_dir(self, file_path, styleSheet = False):
        if os.path.exists(file_path):
            print('Folder already exists')
        else:
            Path(file_path).mkdir(parents=True, exist_ok=True)
            try:
                with open('{}/{}.js'.format(file_path, file_path), mode='w') as f:
                    f.write('import React from "react";')
                    f.write('\n')
                    if styleSheet:
                        f.write('import useStyles from "./{}.styles";'.format(file_path))
                    f.write('\n')
                    f.write('\n')
                    f.write('const test = () => {')
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
                    f.write('export default test')

                    f.close()
            except IOError:
                print('Saving failed!')
            if styleSheet:
                try:
                    with open('{}/{}.styles.js'.format(file_path, file_path), mode='w') as f:
                        f.write('import { makeStyles } from "@material-ui/core";')
                        f.write('\n')
                        f.write('const useStyles = makeStyles((theme) => ({}));')
                        f.write('\n')
                        f.write('export default useStyles;')    
                        f.close()
                except IOError:
                    print('Saving failed!')


    def get_user_choice(self):
        """Prompts the user for its choice and return it."""
        user_input = input('Your choice: ')
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
            print('q: Quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                folder_name = input('Please choose name: ')
                folder_name = self.capitalize_each_word(folder_name)
                self.ensure_dir(folder_name, True)
            if user_choice == '2':
                folder_name = input('Please choose name: ')
                folder_name = self.capitalize_each_word(folder_name)
                self.ensure_dir(folder_name)
            elif user_choice == 'q':
                # This will lead to the loop to exist because it's running condition becomes False
                waiting_for_input = False
            else:
                print('Input was invalid, please pick a value from the list!')
        else:
            print('User left!')

        print('Done!')

if __name__ == '__main__':
    ReactCli = ReactCli()
    ReactCli.listen_for_input()