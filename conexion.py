import mysql.connector
#datos para la conexion a la base de datos

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "user_python"
)
