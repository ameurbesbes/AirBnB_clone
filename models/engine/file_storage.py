#!/usr/bin/python3
"""
"""
import json
from models.base_model import BaseModel

class FileStorage:
	__file_path = "file.json"
	__objects = {}
	
	class_dict = {"BaseModel" : BaseModel}

	def all(self):
		return self.__objects

	def new(self, obj):
		self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

	def save(self):
		my_dict = {}
		for key, obj in self.__objects.items():
			my_dict[key] = obj.to_dict()
		with open( self.__file_path , "w" ) as file:
			json.dump(my_dict, file)

	def reload(self):
		try:
			with open(self.__file_path , "r" ) as file:
				new_obj = json.load(file)
			for key,val in new_obj.items():
				obj = self.class_dict[val['__class__']](**val)
				self.__objects[key] = obj
		except FileNotFoundError:
			pass
