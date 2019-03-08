import pymysql

INSERT_BASIC_DETAILS = '''INSERT INTO Profile (identification_number, identification_type, name, email) VALUES ('{idno}', '{idty}', '{name}', '{email}');'''

def connect():
    return pymysql.connect(
            host='localhost',
            user='hrbotadmin',
            password='#$1!Question',
            db='hrbot',
        )

def save_profile(idno, idty, name, email):
    try:
        connection = connect()
        cursor = connection.cursor()
        insertStatement = INSERT_BASIC_DETAILS.format(idno=idno, idty=idty, name=name, email=email)
        # print(insertStatement)
        cursor.execute(insertStatement)
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except:
        return False
