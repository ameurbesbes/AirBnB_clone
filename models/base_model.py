#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage

"""
"""

time_format = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        """
        if kwargs is not None:
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)
            if kwargs.get('created_at', None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(
                    kwargs['created_at'], time_format)
            else:
                self.created_at = datetime.now()
            if kwargs.get('updated_at', None) and type(self.updated_at) is str:
                self.created_at = datetime.strptime(
                    kwargs['updated_at'], time_format)
            else:
                self.updated_at = datetime.now()
            if kwargs.get(id, None) is None:
                self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        storage.new(self)  # to be checked

    def __str__(self):
        """
        """
        return "[{}] ({}) <{}>".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)

    def save(self):
        """
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        """
        dic = self.__dict__.copy()
        if dic.get('created_at', None) is not None:
            dic['created_at'] = self.created_at.isoformat()
        if dic.get('updated_at', None) is not None:
            dic['updated_at'] = self.created_at.isoformat()
        dic['__class__'] = self.__class__.__name__
        return dic
