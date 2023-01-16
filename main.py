import userdb.sys_db as con
import login.sys_login as login
test = con.opendb()

con.closedb(test)

login.logon()


