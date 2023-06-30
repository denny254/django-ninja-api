from ninja import Schema 
from datetime import datetime


class PostInputSchema(Schema):
    title: str 
    content: str
    
    
class PostOutputSchema(Schema):
    id : int 
    title : str 
    content: str
    created : datetime 