import sqlite3
 
class DataProvider:
    cur: sqlite3.Cursor

    @classmethod
    def initialize(self):
        con = sqlite3.connect("cancerai.db")
        self.cur = con.cursor()

    @classmethod
    def update(cls, attribute_name, new_value):
        if hasattr(cls, attribute_name):
            setattr(cls, attribute_name, new_value)
        else:
            setattr(cls, attribute_name, new_value)

    @classmethod
    def get(cls, attribute_name):
        if hasattr(cls, attribute_name):
            return getattr(cls, attribute_name)
        else:
            raise AttributeError(
                f"'{cls.__name__}' object has no attribute '{attribute_name}'"
            )