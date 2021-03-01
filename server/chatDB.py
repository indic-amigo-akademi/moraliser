import sqlite3
import json
'''
TODO: updateData | deleteData | alterTable
'''


class ChatDB():
    def __init__(self, filename="chat.db"):
        self.__createDB(filename)

    def __createDB(self, filename='chat.db') -> None:
        self.conn = sqlite3.connect(filename)
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def createTable(self, tablename, columns) -> None:
        forList = []
        defList = []
        for col in columns:
            defQuery, forQuery = col.getQuery()
            defList.append(defQuery)
            if forQuery is not None:
                forList.append(forQuery)

        query = f'''
        CREATE TABLE IF NOT EXISTS {tablename} (
            {",".join(defList)}
            {",".join(forList)}
        )
        '''
        print(query)
        self.cur.execute(query)
        self.conn.commit()

    def dropTable(self, tablename) -> None:
        query = f''' DROP TABLE {tablename} '''
        print(query)
        self.cur.execute(query)
        self.conn.commit()

    def insertData(self, tablename, values: dict):
        col_query = ", ".join(values.keys())
        val_query = ", ".join(['?' for i in range(len(values.values()))])
        query = f'''INSERT INTO {tablename}({col_query}) VALUES ({val_query})'''
        print(query)
        self.cur.execute(query, list(values.values()))
        self.conn.commit()

    def updateData(self):
        query = ''
        print(query)


'''
DBColumn for column in SQLite DB
'''


class DBColumn():
    def __init__(self, _name, _type):
        validTypes = ['INTEGER', 'TEXT', 'BLOB', 'NUMERIC', 'REAL']
        self._name = _name
        self._type = _type if _type.upper() in validTypes else 'INTEGER'
        self._notnullable = False
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

    def setNotNullable(self):
        self._notnullable = True
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
            nullable : {self._notnullable.__repr__()}, 
            autoincrement : {self._autoincrement.__repr__()}, 
            unique : {self._unique.__repr__()},
            foreign : {foreign}
        }}'''

    def getQuery(self) -> tuple:
        defQuery = f"{self._name} {self._type} { 'NOT NULL' if self._notnullable else ''} {'PRIMARY KEY' if self._primary else ''} {'AUTOINCREMENT' if self._autoincrement else ''} {'UNIQUE' if self._unique else ''}"
        forQuery = f"FOREIGN KEY({self._name}) REFERENCES {self._foreign['table']}({self._foreign['col']})" if self._foreign else None
        return (defQuery, forQuery)


# chatDatabase = ChatDB()
# columns = [
#     DBColumn('id', 'INTEGER').setAutoincrement().setPrimary().setNotNullable(),
#     DBColumn('username', 'TEXT').setUnique().setNotNullable()
# ]
# chatDatabase.createTable('users', columns)
# chatDatabase.insertData('users', {"username": "shuvamogezel"})
# chatDatabase.close()