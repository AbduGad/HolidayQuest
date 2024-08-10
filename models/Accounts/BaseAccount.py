#!/usr/env python3
import uuid
from datetime import datetime
from typing import List, Dict


class BaseAccount():
    """Class containing base attributes share by child classes
    """

    def __init__(self, email:str, password:str, country:str, created_at:datetime = None,
                 updated_at:datetime = None, id:str = None):
        """Initialize the base account with given attributes."""
        self.email = email
        self.password = password
        self.country = country
        self.__id = id if id is not None else str(uuid.uuid4())
        self.__created_at = created_at if created_at is not None else datetime.utcnow()
        self.updated_at = updated_at if updated_at is not None else datetime.utcnow()


    @property
    def id(self):
        """Return the id of the account."""
        return self.__id

    @property
    def created_at(self):
        """Return the creation timestamp of the account."""
        return self.__created_at
    
    @property
    def email(self):
        """Return the email of the account."""
        return self.__email
    
    @property
    def password(self):
        """Return the password of the account."""
        #####################################
        # Hash function to be added (Un-Hashing)
        #           here
        #####################################
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
        """Validate and set the password of the account."""
        if not isinstance(password, str) or not password:
            raise ValueError("Password must be a non-empty string.")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        #####################################
        # Hash function to be added 
        #           here
        #####################################
        self.__password = password


    
"""
account = BaseAccount(email="test@example.com", password="securepassword", country="USA")

print(account.id)          # Accesses the id property
print(account.email)       # Accesses the email property
print(account.created_at)  # Accesses the created_at property
print(account.password)

account = BaseAccount(email="test@example.com", password="securepassword", country="USA")

print(account.email)  # Prints: test@example.com

account.email = "newemail@example.com"
print(account.email)  # Prints: newemail@example.com
"""