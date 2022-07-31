#-----------------TABLE AND DATABASE CREATION----------------------------
from datetime import date
import mysql.connector as sc

con=sc.connect(host='localhost',user='root',passwd='12345')
if con.is_connected():
    print('Success')
else:
    print('Failed')
cur=con.cursor()
#DATABASE CREATION
cur.execute('Drop database if exists Hospital')
sql='Create database Hospital'
cur.execute(sql)
cur.execute('use Hospital')

#TABLE CREATION
cur.execute('drop table if exists Patient')
cur.execute('drop table if exists Doctor')
cur.execute('drop table if exists Room')
cur.execute('drop table if exists Employee')
cur.execute('drop table if exists Service')
cur.execute('drop table if exists Pharmacy')

datee=str(date.today())

tab1='''create table patient(pid integer primary key, pname varchar(30) not null, age integer(3) not null, gender varchar(10) not null,
        address varchar(40) not null, type varchar(20) default 'out',doa varchar(15) default '{}' )'''.format(datee)
tab2='''create table doctor(did integer primary key, dname varchar(30) not null, qualification varchar(25) not null, specialization varchar(25) not null,
        department varchar(30) not null, experience integer not null, contact_info integer(15) not null, charge integer(10) not null)'''
tab3='''create table room(rid integer(5) primary key, beds integer(5) not null, availability varchar(10) not null, charge integer(10) not null,
        type varchar(30) not null)'''
tab4='''create table employee(eid integer(5) primary key, ename varchar(30) not null, field varchar(30) not null, contact_info integer(15) not null)'''
tab5='''create table service(sid integer(5) primary key, s_name varchar(30) not null, charge integer(10) not null)'''
tab6='''create table pharmacy(med_id integer(5) primary key, med_name varchar(30) not null, quantity integer(5) not null, rate integer not null)'''

cur.execute(tab1)
cur.execute(tab2)
cur.execute(tab3)
cur.execute(tab4)
cur.execute(tab5)
cur.execute(tab6)
print('DOne')
