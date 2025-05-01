from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    """
    Contains the logic for the GUI,
    Takes in plaintext and shift number input,
    outputs a shifted text.
    """
    def __init__(self) -> None:
        """
        Initializes the GUI.
        """
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda: self.submit())

    def submit(self) -> None:
        """
        Gets plaintext and shift number,
        gets the selected alphabet
        applies shift to text and outputs shifted text.
        """
        self.__plaintext = self.text_input.text()
        self.__shift_num = self.shift_input.text().strip()
        self.__shifttext = ''

        if self.az_radio.isChecked():
            self.__alphabet = 1
        elif self.az09_radio.isChecked():
            self.__alphabet = 2
        elif self.az09_radio_2.isChecked():
            self.__alphabet = 3
        elif self.az09_radio_3.isChecked():
            self.__alphabet = 4
        else:
            self.__alphabet = 5

        try:
            if self.__alphabet == 1:
                for letter in self.__plaintext:
                    if letter.isupper():
                        index = ord(letter)
                        for i in range(int(self.__shift_num)):
                            index += 1
                            if index == 91:
                                index = 65
                        self.__shifttext += chr(index)
                    elif letter.islower():
                        index = ord(letter)
                        for i in range(int(self.__shift_num)):
                            index += 1
                            if index == 123:
                                index = 97
                        self.__shifttext += chr(index)
                    else:
                        self.__shifttext += letter
            elif self.__alphabet == 2:
                for letter in self.__plaintext:
                    if letter.isupper():
                        index = ord(letter)
                        for i in range(int(self.__shift_num)):
                            index += 1
                            if index == 91:
                                index = 48
                            elif index == 58:
                                index = 65
                        self.__shifttext += chr(index)
                    elif letter.islower():
                        index = ord(letter)
                        for i in range(int(self.__shift_num)):
                            index += 1
                            if index == 123:
                                index = 97
                        self.__shifttext += chr(index)
                    elif letter.isdigit():
                        index = ord(letter)
                        for i in range(int(self.__shift_num)):
                            index += 1
                            if index == 58:
                                index = 65
                            if index == 91:
                                index = 48
                        self.__shifttext += chr(index)
                    else:
                        self.__shifttext += letter
            elif self.__alphabet == 3:
                for letter in self.__plaintext:
                    if letter.isupper():
                        index = ord(letter)
                        for i in range(int(self.__shift_num)):
                            index += 1
                            if index == 91:
                                index = 65
                        self.__shifttext += chr(index)
                    elif letter.islower():
                        index = ord(letter)
                        for i in range(int(self.__shift_num)):
                            index += 1
                            if index == 123:
                                index = 48
                            elif index == 58:
                                index = 97
                        self.__shifttext += chr(index)
                    elif letter.isdigit():
                        index = ord(letter)
                        for i in range(int(self.__shift_num)):
                            index += 1
                            if index == 58:
                                index = 97
                        self.__shifttext += chr(index)
                    else:
                        self.__shifttext += letter
            elif self.__alphabet == 4:
                for letter in self.__plaintext:
                    if letter.isupper():
                        index = ord(letter)
                        for i in range(int(self.__shift_num)):
                            index += 1
                            if index == 91:
                                index = 65
                        self.__shifttext += chr(index)
                    elif letter.islower():
                        index = ord(letter)
                        for i in range(int(self.__shift_num)):
                            index += 1
                            if index == 123:
                                index = 97
                        self.__shifttext += chr(index)
                    elif letter.isdigit():
                        index = ord(letter)
                        for i in range(int(self.__shift_num)):
                            index += 1
                            if index == 58:
                                index = 48
                        self.__shifttext += chr(index)
                    else:
                        self.__shifttext += letter
            else:
                for letter in self.__plaintext:
                    index = ord(letter)
                    for i in range(int(self.__shift_num)):
                        index += 1
                        if index == 127:
                            index = 32
                    self.__shifttext += chr(index)

            with open('cipher.txt', 'a') as file:
                file.write(self.__shifttext)

            self.ciphertext.setText(self.__shifttext)

        except TypeError:
            self.ciphertext.setText('Shift number must be an integer.')