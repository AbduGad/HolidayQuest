from models import BaseModel


class Post(BaseModel):
    """Post model"""
    def __init__(self, live:bool = True):
        self.live = live