import sqlite3
 
class DataProvider:
    cur: sqlite3.Cursor

    @classmethod
    def initialize(self):
        con = sqlite3.connect("cancerai.db")
        self.cur = con.cursor()
