#!/usr/env python3
from BaseAccount import BaseAccount
from datetime import datetime



class User(BaseAccount):
    """ User class handling normal user able to book trips hotels etc..
    """
    counter = 0
    def __init__(self, FirstName:str, LastName:str, email:str, password:str,
              id:str, created_at:datetime, updated_at:datetime, country:str, ProfilePicture:str):
        """Initializes a new User object.
        """
        self.FirstName = FirstName
        self.LastName =LastName
        User.counter+=1
        super.__init__(email, password, id, created_at, updated_at, country, ProfilePicture)

    @property
    def FirstName(self):
        """ Gets the first name of the user."""
        return self.__FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        """ Sets the first name of the user."""
        if not FirstName:
            raise ValueError("First name cannot be empty")
        self.__FirstName = FirstName

    @property
    def LastName(self):
        """ Gets the last name of the user."""
        return self.__LastName
    
    @LastName.setter
    def LastName(self, LastName):
        """ Sets the last name of the user."""
        if not LastName:
            raise ValueError("Last name cannot be empty")
        self.__LastName = LastName
