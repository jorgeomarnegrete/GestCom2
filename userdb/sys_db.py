#--------------------------------------#
# Archivo para manejo de base de datos #
# Autor: Jorge O. Negrete              #
# Fecha: 16-01-2023                    #
#--------------------------------------#

import mysql.connector as db
def opendb():
    # Apertura de base de datos #

    db_con = db.connect(host='localhost', port='3306',
                        user='root', password='admin', database='gcdb')

    return db_con


def closedb( dbname ):
    # Cierre de base de datos #

    dbname.close()



