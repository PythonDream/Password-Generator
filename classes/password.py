import random
import string


class PasswordGenerator():
    # Numbers
    numbers = string.digits
    # Lower case characters
    chars = string.ascii_lowercase
    # Special chars
    specialChars = string.punctuation

    functions = [str.lower, str.upper]
    # Todo
    # return strings for python 3
    # return strings for python 2
    # x chars random password upper, lower, and digits
    # x chars random password upper, lower, specialChars, and digits
    # x chars random password upper, lower, and digits + words mixed in

    def characters(self, chars):
        """This methods returns the designated characters
        s = special characters
        n = numbers 0-9
        l = a-z (lowercase)
        u = A-Z (uppercase)"""
        characters = ''
        if chars:
            chars = list(chars.lower())
            used = 0
            for char in chars:
                if char == 'n':
                    characters += self.numbers

                if char == 'l' or char == 'u' and used < 1:
                    characters += self.chars
                    used += 1

                if char == 's':
                    characters += self.specialChars

    def random_password(self, chars, size):
        if chars:
            functions = self.functions
            # check if both lowercase and uppercase characters is demanded
            if 'l' not in chars or 'u' not in chars:
                if 'l' not in chars:
                    functions.remove(str.lower)
                if 'u' not in chars:
                    functions.remove(str.upper)

            chars = self.characters(chars)

            password = list()

            for _ in range(size):
                char = random.choice(self.chars)

                if char.isalpha():
                    password.append(random.choice(self.functions)(char))
                else:
                    password.append(char)
        else:
            raise Exception('chars cant be null')
            
        return ''.join(password)

    def shuffle_words(self, words):
        words = words.split()
        random.shuffle(words)
        return words

    def shuffle_letters(self, words):
        words = list(words.replace(' ', ''))
        random.shuffle(words)
        return words

    def random_upper_lower(self, func, words):
        if func:
            if func.lower() == 'shuffle_letters':
                words = self.shuffle_letters(words)
            if func.lower() == 'shuffle_words':
                words = self.shuffle_words(words)
        else:
            raise ValueError('func cant be empty')

        password = ''.join(random.choice(self.functions)(letter) for letter in words)

        return password
