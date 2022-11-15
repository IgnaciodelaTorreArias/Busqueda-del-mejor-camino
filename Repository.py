import sqlite3

class Repository:
    def __init__(self, database:str):
        self.__data = sqlite3.connect(database)
        self.__cursor = self.__data.cursor()
        self.__cursor.executescript("""
            CREATE TABLE IF NOT EXISTS nodos(
                id      INTEGER     PRIMARY KEY AUTOINCREMENT,
                name    VARCHAR(15) NOT NULL
            );

            CREATE INDEX IF NOT EXISTS nodesID ON nodos (id);
            
            CREATE TABLE IF NOT EXISTS conexiones(
                punto1  INTEGER NOT NULL,
                punto2  INTEGER NOT NULL,
                peso    INTEGER NOT NULL,
                FOREIGN KEY(punto1) REFERENCES nodos(id)
                FOREIGN KEY(punto2) REFERENCES nodos(id)
            );
        """)
        self.__data.commit()

    #Consulta de existencia
    def buscarExistenciaPorNombre(self, name:str)-> bool:
        self.__cursor.execute(f"SELECT * FROM nodos WHERE name = '{name}'")
        if len(self.__cursor.fetchall()) == 0: return False
        return True

    def buscarExistenciaPorId(self, id:int)-> bool:
        self.__cursor.execute(f"SELECT * FROM nodos WHERE id = {id}")
        if len(self.__cursor.fetchall()) == 0: return False
        return True

    def seConectan(self, id1:int, id2:int)->bool:
        self.__cursor.execute(f"SELECT * FROM conexiones WHERE (punto1 = {id1} AND punto2 = {id2}) OR (punto1 = {id2} AND punto2 = {id1})")
        if len(self.__cursor.fetchall()) == 0: return False
        return True

    #Creacion y modificacion de nodos
    def agregarNodo(self, name:str)-> None:
        self.__cursor.execute(f"INSERT INTO nodos (name) VALUES ('{name}')")
        self.__data.commit()

    def cambiarNombre(self, id:int, newName:str)->None:
        self.__cursor.execute(f"UPDATE nodos SET name = '{newName}' WHERE id = {id}")

    #Creacion y modificacion de conexiones
    def conectar(self, id1: int, id2:int, peso:int)-> None:
        self.__cursor.execute(f"INSERT INTO conexiones (punto1, punto2, peso) VALUES ({id1}, {id2}, {peso})")
        self.__data.commit()

    def editarConexion(self, id1:int, id2:int, peso:int)-> None:
        self.__cursor.execute(f"UPDATE conexiones SET peso = {peso} WHERE (punto1={id1} AND punto2={id2}) OR (punto1={id2} AND punto2={id1})")
        self.__data.commit()

    #Eliminacion de datos
    def eliminarNodo(self, id:int)-> None:
        self.aislarNodo(id)
        self.__cursor.execute(f"DELETE FROM nodos WHERE id = {id}")
        self.__data.commit()

    def eliminarConexion(self, id1:int, id2:int)-> None:
        self.__cursor.execute(f"DELETE FROM conexiones WHERE (punto1={id1} AND punto2={id2}) OR (punto1={id2} AND punto2={id1})")
        self.__data.commit()

    def aislarNodo(self, id:int)-> None:
        self.__cursor.execute(f"DELETE FROM conexiones WHERE punto1 = {id} OR punto2 = {id}")
        self.__data.commit()

    #Recuperacion de datos
    def getNodos(self)-> list:
        self.__cursor.execute("SELECT id, name FROM nodos")
        return self.__cursor.fetchall()

    def getConexiones(self)-> list:
        self.__cursor.execute("SELECT punto1, punto2, peso FROM conexiones")
        return self.__cursor.fetchall()

    def getConexionesNombres(self)-> list:
        self.__cursor.execute("SELECT a.name, b.name, peso FROM conexiones INNER JOIN nodos a ON a.id = punto1 INNER JOIN nodos b ON b.id = punto2;")
        return self.__cursor.fetchall()

    def getName(self, id:int )->str:
        self.__cursor.execute(f"SELECT name FROM nodos WHERE id = {id}")
        name = self.__cursor.fetchall()
        if len(name) == 0: return None
        return name[0][0]

    def getId(self, name:str)->int:
        self.__cursor.execute(f"SELECT id FROM nodos WHERE name = '{name}'")
        ID = self.__cursor.fetchall()
        if len(ID) == 0: return None
        return ID[0][0]

    def whoConnects(self, origin:int )->list:
        self.__cursor.execute(f"SELECT punto1, punto2, peso FROM conexiones WHERE punto1 = {origin} OR punto2 = {origin} ORDER BY peso")
        result = []
        for item in self.__cursor.fetchall():
            result.append((item[1], item[2])) if item[0] == origin else result.append((item[0], item[2]))
        return result

    #Limpieza de base de datos
    def limpiar(self)->None:
        self.__cursor.execute(f"DELETE FROM conexiones")
        self.__cursor.execute(f"DELETE FROM nodos")
        self.__data.commit()

    def reiniciar(self)->None:
        self.__cursor.execute(f"DELETE FROM conexiones")
        self.__cursor.execute(f"DELETE FROM nodos")
        self.__cursor.execute(f"UPDATE sqlite_sequence SET seq = 0 WHERE name = 'nodos'")
        self.__data.commit()