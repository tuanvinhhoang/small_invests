import pandas as pd
import sqlalchemy
import pyodbc

driver = 'ODBC Driver 17 for SQL Server'
server = 'DESKTOP-DETHBRG'
database = 'hack'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
                     SERVER=' + server + ' ; \
                     DATABASE=' + database + ';\
                     Trusted_Connection=yes;')

cursor = conn.cursor()


def main(entrepreneur,investor):
    if entrepreneur:
        ename = str(input('Please enter your name'))
        ebudget = int(input('Please enter budget required'))
        eindustry = str(input('Enter your industry'))

        sql_code = ('''
                insert into [hack].[dbo].[entrepreneur] values (?,?,?)
                ''')
        val = (ename, ebudget, eindustry)
        cursor.execute(sql_code, val)
        conn.commit()

        sql_select='''
        select * from [hack].[dbo].[investor]
        where InvIndustry = '%s'
        ''' % eindustry
        df=pd.read_sql(sql_select,conn)
        print("The potential investors are:")
        print (df)



    elif(investor):
        invname = input('Please enter your name')
        minbudget = int(input('Please enter minimum amount to invest'))
        maxbudget = int(input('Please enter maximum amount to invest'))
        invindustry = input('Enter industry you are willing to invest')

        sql_code = ('''
                insert into [hack].[dbo].[investor] values (?,?,?,?)
                ''')
        val = (invname, minbudget,maxbudget, invindustry)
        cursor.execute(sql_code, val)
        conn.commit()

        sql_select = '''
                select * from [hack].[dbo].[entrepreneur]
                where EIndustry = '%s'
                ''' % invindustry
        df = pd.read_sql(sql_select, conn)
        print("The potential entrepreneurs are:")
        print(df)



