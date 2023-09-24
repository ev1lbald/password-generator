from random import choice
import string

digits = string.digits  # Символы
lowercases = string.ascii_lowercase
uppercases = string.ascii_uppercase
punctuation = '!#$%&*+-=?@^_'
chars = ''

def good_password(passwords): 
    good_passwords = []
    for i in range (len(passwords)):
        if any(c.isdigit() for c in passwords[i]) and any(c.islower() for c in passwords[i]) and any(c.isupper() for c in passwords[i]):
            good_passwords.append(passwords[i])
    return good_passwords
        
def create_password(number, length):
    passwords = []
    
    for i in range(number):
        password = ''
        password_chars = [choice(chars) for _ in range(length)]        
        password = ''.join(password_chars)
        passwords.append(password)
    
    return passwords
# Ввод
num = int(input('How many passwords do you need? ')) 
length = int(input('What should be the length of each password? '))
if input('Include digits 0123456789? (yes/no): ').lower() == 'yes':
    chars += digits
if input('Include uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ? (yes/no): ').lower() == 'yes':
    chars += uppercases
if input('Include lowercase letters abcdefghijklmnopqrstuvwxyz? (yes/no): ').lower() == 'yes':
    chars += lowercases
if input('Include symbols !#$%&*+-=?@^_? (yes/no): ').lower() == 'yes':
    chars += punctuation

passwords = create_password(num, length)
result = good_password(passwords)
good_or_all = input('Should the password be good? (good/all): ').lower()



file_or_no = input('Do you want to write passwords to the file? (yes/no): ')
if file_or_no.lower() == 'yes':
    file_name = input('Input file name or place where to create it ')
    for i in range(len(passwords)):
        passwords[i] += '\n'
    with open(f'{file_name}', 'w', encoding='utf-8') as file:
        file.writelines(passwords)
elif file_or_no.lower() == 'no':
    if good_or_all == 'good':  #Вывод
        if len(result) > 0:
           print('Here is good passwords:')
           print(*result, sep='\n')
        else:
            print('There was no good passwords generated.')
    elif good_or_all == 'all':
        print(*passwords, sep='\n')