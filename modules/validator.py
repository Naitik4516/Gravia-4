import re
from phonenumbers import geocoder
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type

class invalidCountryCode(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class validatePhonenumber:
    def check(phonenumber):
        try:
            check = carrier._is_mobile(number_type(phonenumbers.parse(phonenumber)))
            return check
        except Exception:
            raise invalidCountryCode()
    def getCountry(phonenumber):
        my_number = phonenumbers.parse(phonenumber)
        country = geocoder.description_for_number(my_number,"en")
        return country

class validateEmail:
    def check(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return True
        else:
            return False

# Password validation in Python
# using naive method

# Function to validate the password
class validatePassword: 
    def check(password):
        SpecialSym =['$', '@', '#', '%']
        val = True
        
        if len(password) < 6:
            print('length should be at least 6')
            val = False
            
        if not any(char.isdigit() for char in password):
            print('Password should have at least one numeral')
            val = False
            
        if not any(char.isupper() for char in password):
            print('Password should have at least one uppercase letter')
            val = False
            
        if not any(char.islower() for char in password):
            print('Password should have at least one lowercase letter')
            val = False
            
        if not any(char in SpecialSym for char in password):
            print('Password should have at least one of the symbols $@#')
            val = False
        if val:
            return val
        else:
            return False

# Driver Code
if __name__ == '__main__':
    a = validatePassword.check("Hhellodh@d54hdhd")
    if a != True:
        print("Not valid")
    else: print("valid")