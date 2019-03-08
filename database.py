import pymysql

INSERT_BASIC_DETAILS = '''INSERT INTO Profile
(first_name, middle_name, last_name, email, contact,
dob, addr, exprnc, skills, resume_path)
VALUES ('{fn}', '{mn}', '{ln}', '{email}', '{contact}', '{dob}', '{addr}',
'{exprnc}', '{skills}', '{resume_path}');'''

def connect():
    return pymysql.connect(
            host='localhost',
            user='hrbotadmin',
            password='#$1!Question',
            db='hrbot',
        )

def get_last_profile():
    #
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM Profile ORDER BY id DESC LIMIT 1;")
    value = cursor.fetchone()
    try:
        return value[0]
    except:
        return 0

def save_profile(fn, ln, mn, dob, addrs, email, contact, exprnc, skills, resume):
    try:
        # print(idno)
        connection = connect()
        cursor = connection.cursor()
        insertStatement = INSERT_BASIC_DETAILS.format(fn=fn, mn=mn, ln=ln, email=email, contact=contact, dob=dob, addr=addrs, exprnc=exprnc, skills=skills, resume_path=resume)
        # print(insertStatement)
        cursor.execute(insertStatement)
        connection.commit()
        # print(select_statement)
        cursor.execute("SELECT id FROM Profile ORDER BY id DESC LIMIT 1;")
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
