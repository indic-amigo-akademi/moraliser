import sqlite3
import json
'''
TODO: createTable | deleteTable | insertData | updateData | deleteData | alterTable
'''


class ChatDB():
    def __init__(self, filename="chat.db"):
        self.createDB(filename)

    def createDB(self, filename='chat.db') -> None:
        self.conn = sqlite3.connect(filename)
        self.cur = self.conn.cursor()

    def createTable(self, tablename, columns):
        query = f'''
        CREATE TABLE IF NOT EXISTS {tablename}
        '''


'''
DBColumn for column in SQLite DB
'''


class DBColumn():
    def __init__(self, _name, _type):
        validTypes = ['INTEGER', 'TEXT', 'BLOB', 'NUMERIC', 'REAL']
        self._name = _name
        self._type = _type if _type.upper() in validTypes else 'INTEGER'
        self._nullable = False
        self._autoincrement = False
        self._unique = False
        self._primary = False
        self._foreign = None

    def setUnique(self):
        self._unique = True
        return self

    def setPrimary(self):
        self._primary = True
        return self

    def setAutoincrement(self):
        self._autoincrement = True
        return self

    def setNullable(self):
        self._nullable = True
        return self

    def setForeign(self, tablename, col):
        self._foreign = {"table": tablename, "col": col}
        return self

    def __str__(self):
        foreign = "None"
        if self._foreign != None:
            foreign = f'''{{
                table : {self._foreign['table'].__repr__()},
                col : {self._foreign['col'].__repr__()}
            }}
            '''
        return f''' {{ 
            name : {self._name.__repr__()}, 
            type : {self._type.__repr__()}, 
            nullable : {self._nullable.__repr__()}, 
            autoincrement : {self._autoincrement.__repr__()}, 
            unique : {self._unique.__repr__()},
            foreign : {foreign}
        }}'''
