import pymysql

INSERT_BASIC_DETAILS = '''INSERT INTO Profile (identification_number, identification_type, name, email) VALUES ('{idno}', '{idty}', '{name}', '{email}');'''
GET_DETAILS = '''select id from Profile where identification_number='{idno}' and identification_type='{idty}' and name='{name}' and email='{email}';'''

def connect():
    return pymysql.connect(
            host='localhost',
            user='hrbotadmin',
            password='#$1!Question',
            db='hrbot',
        )

def save_profile(idno, idty, name, email):
    try:
        # print(idno)
        connection = connect()
        cursor = connection.cursor()
        insertStatement = INSERT_BASIC_DETAILS.format(idno=idno, idty=idty, name=name, email=email)
        # print(insertStatement)
        cursor.execute(insertStatement)
        connection.commit()
        select_statement = GET_DETAILS.format(idno=idno, idty=idty, name=name, email=email)
        # print(select_statement)
        cursor.execute(select_statement)
        # print(cursor.fetchall())
        value = cursor.fetchone()
        connection.close()
        return {"status": True, "user_id": value[0]}
    except KeyError as ke:
        print(ke)
        return False
    except:
        return False


def save_user_qsn_answer():
    pass
