#!/usr/bin/python3
import uuid
from datetime import datetime


time = "%Y-%m-%dT%H:%M:%S"

class	BaseModel():
    """Class containing attributes needed for other classes"""

    def __init__(self, id:str, created_at:str, updated_at:str):
        """sets shared attributes between other classes"""
        self.__id = id if id is not None else str(uuid.uuid4())
        self.__created_at = datetime.strptime(created_at, time) if created_at is not None else datetime.utcnow()
        self.__updated_at = datetime.strptime(updated_at, time) if updated_at is not None else datetime.utcnow()

    @property
    def id(self):
        """Return the id of the account."""
        return self.__id
    
    @property
    def created_at(self):
        """Return the creation timestamp of the account."""
        return self.__created_at
    
    @property
    def updated_at(self):
        return self.__updated_at
    
    @created_at.setter
    def created_at(self, created_at):
        """Set the creation timestamp of the account."""
    
    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        for key, value in self.__dict__.items():
            if key != '_sa_instance_state':
                if isinstance(value, datetime):
                    dictionary[key] = value.isoformat()
                else:
                    dictionary[key] = value
        dictionary['__class__'] = self.__class__.__name__
        return dictionary

created_at = None     
created_at = datetime.strptime(created_at, time) if created_at is not None else datetime.utcnow()
print(created_at)
created_at = datetime.strptime(created_at, time) if created_at is not None else datetime.utcnow()
print(created_at)