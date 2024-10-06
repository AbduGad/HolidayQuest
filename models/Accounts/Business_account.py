#!/usr/env python3
from models.Accounts import BaseAccount
from typing import List, Dict
from models import Post, Rating, Review


class Business(BaseAccount):
    """
    Account for companies/trip planners to post their trips/ promotions
    """
    counter = 0
    def __init__(self, email:str, password:str, country:str, created_at:str,
                 updated_at:str, id:str, ProfilePicture:str, Business_name:str,
                 Business_address:str):
        self.Business_name= Business_name
        self.Business_address = Business_address
        self.country = country
        Business.counter+=1
        super.__init__(email, password, created_at, updated_at, id, ProfilePicture)

    @property
    def Business_name(self):
        return self.__Business_name
    
    @property
    def Business_address(self):
        return self.__Business_address
    
    @property
    def country(self):
        return self.__country
    
    @Business_name.setter
    def Business_name(self, Business_name):
        if not Business_name:
            raise ValueError("Business name cannot be empty.")
        self.__Business_name = Business_name
        
    @Business_address.setter
    def Business_address(self, Business_address):
        if not Business_address:
            raise ValueError("Address field can not be empty.")
        self.__Business_address = Business_address

    @country.setter
    def country(self, country):
        if not country:
            raise ValueError("Country field cannot be empty.")
