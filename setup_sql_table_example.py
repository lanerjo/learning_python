#sqlite connect and interact with db
#sqlite db name test.sqlite
#sqlite db location c:\python27\
#db tables = users (name)
import sqlite3 #imports sqlite module
conn = sqlite3.connect('test.sqlite') #connects to the test.sqlite db
c = conn.cursor()
#variable define section
tablename1 = 'users'
newfield = 'username'
newfield1 = 'password'
newfield2 = 'assigned_port'
newfield3 = 'lat'
newfield4 = 'long'
newfield5 = 'steps'
newfield6 = 'dummylogin'
newfield7 = 'dummyint'
newfield8 = 'dummypass'
newfield9 = 'fname'
fieldtype1 = 'INTEGER'
fieldtype2 = 'STRING'
fieldtype3 = 'FLOAT'

#creating a new sqlite column for each required field
c.execute('alter table {tn} add columm {cn} {ct}'\
    .format(tn=tablename1, cn = newfield9, ct=fieldtype2))
c.execute('alter table {tn} add column {cn} {ct}'\
    .format(tn=tablename1, cn=newfield, ct=fieldtype2))
c.execute('alter table {tn} add column {cn} {ct}'\
    .format(tn=tablename1, cn=newfield1, ct=fieldtype2))
c.execute('alter table {tn} add column {cn} {ct}'\
    .format(tn=tablename1, cn=newfield2, ct=fieldtype1))
c.execute('alter table {tn} add column {cn} {ct}'\
    .format(tn=tablename1, cn=newfield3, ct=fieldtype3))
c.execute('alter table {tn} add column {cn} {ct}'\
    .format(tn=tablename1, cn=newfield4, ct=fieldtype3))
c.execute('alter table {tn} add column {cn} {ct}'\
    .format(tn=tablename1, cn=newfield5, ct=fieldtype1))
c.execute('alter table {tn} add column {cn} {ct}'\
    .format(tn=tablename1, cn=newfield6, ct=fieldtype2))
c.execute('alter table {tn} add column {cn} {ct}'\
    .format(tn=tablename1, cn=newfield7, ct=fieldtype1))
c.execute('alter table {tn} add column {cn} {ct}'\
    .format(tn=tablename1, cn=newfield8, ct=fieldtype2))




conn.commit() #commits (saves) changes to the db
conn.close() #closes the connection to the db