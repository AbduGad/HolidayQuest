#!/usr/env python3
import uuid
from models import BaseModel
from datetime import datetime
from typing import List, Dict
from bson import ObjectId # type: ignore
from bcrypt import hashpw, gensalt, checkpw # type: ignore



class BaseAccount(BaseModel):
    """Class containing base attributes share by child classes
    """
    def __init__(self, email:str, password:str, country:str, created_at:datetime = None,
                 updated_at:datetime = None, id:str = None, ProfilePicture:str = "default.png"):
        """Initialize the base account with given attributes.
        
        Profile Picture: is only the file name ( the path is fixed)
        """
        self.email = email
        self.password = password
        self.country = country
        self.ProfilrPicture = ProfilePicture
        super.__init__(id, created_at, updated_at)

    @property
    def email(self):
        """Return the email of the account."""
        return self.__email
    
    @property
    def password(self):
        """Return the hashed string password of the account."""
        return self.__password

    @email.setter
    def email(self, email):
        """Validate and set the email of the account."""
        if not isinstance(email, str) or not email:
            raise ValueError("Email must be a non-empty string.")
        if '@' not in email:
            raise ValueError("Email must contain '@'.")
        self.__email = email

    @password.setter
    def password(self, password):
        """Validate, hash and set the password of the account as a string."""
        if not isinstance(password, str) or not password:
            raise ValueError("Password must be a non-empty string.")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        #####################################
        # Hash function
        # endoce() change the password to bytes before hashing with key gensalt()
        # then decode() is called to store it as a string instead of bytes for easier use
        #####################################
        hashed_password = hashpw(password.encode(), gensalt()).decode()
        self.__password = hashed_password

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        for key, value in self.__dict__.items():
            if key != '_id' and isinstance(value, ObjectId):
                if isinstance(value, datetime):
                    dictionary[key] = value.isoformat()
                else:
                    dictionary[key] = value
        dictionary['__class__'] = self.__class__.__name__
        return dictionary
    
    def delete():
        """delete the current object from the storage"""
        # Yet to be implemented depends on storage

###################################################    
# account = BaseAccount(email="test@example.com", password="securepassword", country="USA")

# print(account.id)          # Accesses the id property
# print(account.email)       # Accesses the email property
# print(account.created_at)  # Accesses the created_at property
# print(account.password)

# account = BaseAccount(email="test@example.com", password="securepassword", country="USA")

# print(account.email)  # Prints: test@example.com

# account.email = "newemail@example.com"
# print(account.email)  # Prints: newemail@example.com
# print(ObjectId())

##################################################
# password = b"super secret password"
# # Hash a password for the first time, with a randomly-generated salt
# hashed = hashpw(password, gensalt())
# # Check that an unhashed password matches one that has previously been
# # hashed
# print (hashed)
# if checkpw(password, hashed):
#     print("It Matches!")
# else:
#     print("It Does not Match :(")

####################--bcrypt.decode()--#############################
# # Password and hashing
# password = b"super secret password"
# hashed = hashpw(password, gensalt())
# print(hashed)

# # Decoding example if needed
# decoded_hashed = hashed.decode()
# print(decoded_hashed)

#####################--bcrypt.checkpw() example--################################
# # Hash a password (for registration or password change)
# def hash_password(password: str) -> bytes:
#     return hashpw(password.encode(), gensalt())

# # Check if the provided password matches the stored hash (for login)
# def check_password(stored_hash: bytes, password: str) -> bool:
#     return checkpw(password.encode(), stored_hash)

# # Example usage
# password = "my_secure_password"
# hashed_password = hash_password(password)

# # At login, you would use:
# if checkpw(password.encode(), hashed_password):
#     print("Password matches!")
# else:
#     print("Password does not match.")
