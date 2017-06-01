from classes.password import PasswordGenerator
test = PasswordGenerator()

#for _ in range(20):
print(test.random_password('nls', 5))
print(test.random_password('nls', 5))
print(test.random_upper_lower('shuffle_letters', 'Alexander Lausten'))
print(test.random_upper_lower('shuffle_words', 'Alexander Lausten'))
