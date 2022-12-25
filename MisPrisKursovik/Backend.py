import pymysql
class Backend():
  def conToDat(self):
    con = pymysql.connect(host="localhost",
      user="root",
      password="Golang13112!",
      database="lab3", )
    # cursorclass=pymysql.cursors.DictCursor)
    return con

  def select(self, con, tableName):
    with con.cursor() as cursor:
      sql = f"SELECT * FROM {tableName}"
      cursor.execute(sql)
      rows = cursor.fetchall()
      colLen = len(rows[0])
      colName = self.getColumnName(con, tableName)
      return rows, colName

  def getTablesNames(self, con):
    with con.cursor() as cursor:
      sql = "SHOW TABLES;"
      cursor.execute(sql)
    return [i[0] for i in cursor.fetchall()]


  def getColumnName(self, con, tableName):
    with con.cursor() as cursor:
      sql = f"SHOW columns FROM {tableName};"
      cursor.execute(sql)
      return [i[0] for i in cursor.fetchall()]

  def READ_VAR_CONF(self, con, idProd):
    parNameList = []
    with con.cursor() as cursor:
      findClass = f"SELECT ID_CLASS FROM PROD WHERE ID_PROD = {idProd} AND CONF = 2;"
      cursor.execute(findClass)
      idClass = cursor.fetchone()
      if idClass == None:
        return 1

      findParId = f"SELECT ID_PAR FROM PARAM_PROD_CLASSIFICATOR WHERE ID_CLASS = {idClass[0]};"
      cursor.execute(findParId)
      params = cursor.fetchall()
      for param in params:
        findParName = f"SELECT * FROM PARAM WHERE ID_PAR = {param[0]};"
        cursor.execute(findParName)
        parName = cursor.fetchone()
        parNameList.append(parName)
    return parNameList

  def INS_ORDER(self, con, customerId, date, num):
    with con.cursor() as cursor:
      sql = f"INSERT INTO ORDER1(NUM,DATE_REG,CUSTOMER) VALUES('{num}','{date}',{customerId});"
      try:
        cursor.execute(sql)
      except (pymysql.err.ProgrammingError, pymysql.err.OperationalError, pymysql.err.IntegrityError) as e:
        con.close()
        return e
      else:
        con.commit()

  def WRITE_PAR2(self, con, idProd, idPar, Q):
    with con.cursor() as cursor:
      try:
        sql = f"CALL WRITE_PAR2({idProd},{idPar},{Q});"
        cursor.execute(sql)
      except (pymysql.err.ProgrammingError, pymysql.err.OperationalError, pymysql.err.IntegrityError) as e:
        con.close()
        return e
      else:
        con.commit()

  def NEW_VAR_PROD(self, con, idProd):
    with con.cursor() as cursor:
      try:
        sql = f"CALL NEW_VAR_PROD({idProd},@id,@name);"
        cursor.execute(sql)
      except (pymysql.err.ProgrammingError, pymysql.err.OperationalError, pymysql.err.IntegrityError) as e:
        con.close()
        return e
      else:
        con.commit()

  def ADD_PROD(self, con, name, id_class, conf, type_prod):
    with con.cursor() as cursor:
      sql = f"insert PROD(NAME, ID_CLASS, CONF, TYPE_PROD) values ('{name}', {id_class}, {conf}, {type_prod});"
      cursor.execute(sql)
    con.commit()


  def ADD_PROD_ORDER(self, con, idOrder, idProd, Q):
    with con.cursor() as cursor:
      try:
        sql = f"CALL ADD_PROD_ORDER({idOrder},{idProd},{Q});"
        cursor.execute(sql)
      except (pymysql.err.ProgrammingError, pymysql.err.OperationalError, pymysql.err.IntegrityError) as e:
        con.close()
        return e
      else:
        con.commit()