# USES
from collections import deque

# interface


class PalindromeVerifier:
    def __init__(self, Again='y', WoN=None):
        str.lower(Again)
        while Again != 'n':
            WoN = str.lower(input('Write the word or number: '))
            self.Edeque = deque(WoN)
            self.Rdeque = self.Edeque.copy()
            self.Rdeque.reverse()
            # self.Edeque = str(self.Edeque)
            # self.Rdeque = str(self.Rdeque)
            if self.Rdeque == self.Edeque:
                print('This is a palidrome!')
            else:
                print('This is not a palidrome!')
            WoNr = ''
            for element in self.Rdeque:
                WoNr = WoNr + str(element)

            print('The reverse caracters of '+WoN + ' is ' + WoNr)
            print('Press Y, to verify another word, or press N to exit!')
            Again = input(': ')
            str.lower(Again)
            while (str.lower(Again) != 'n') and (str.lower(Again) != 'y'):
                print('Press Y, to verify another word, or press N to exit!')
                Again = str.lower(input(': '))
                # Again = str.lower(Again)
        exit


# implementation
Verifier = PalindromeVerifier()
