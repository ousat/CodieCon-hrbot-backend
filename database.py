import pymysql

INSERT_BASIC_DETAILS = '''INSERT INTO Profile
(name, email, password, resume_path)
VALUES ('{fn}', '{email}','{pwd}', '{resume_path}');'''

def connect():
    return pymysql.connect(
            host='localhost',
            user='hrbotadmin',
            password='#$1!Question',
            db='hrbot',
        )


def validate(email, password):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT id, email, password FROM Profile ORDER BY id DESC;")

    value = cursor.fetchall()
    # print(value)
    for user_entry in value:
        # print(user_entry)
        if user_entry[1] == email and user_entry[2] == password:
            return {"status": True, "id": user_entry[0]}

    connection.close()
    return {"status": False}


def get_file_name(id):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT resume_path FROM Profile WHERE id="+str(id)+" ORDER BY id DESC;")

    value = cursor.fetchone()
    # print(value)
    connection.close()
    resume_entry = value[0]
    return resume_entry


def select_questions(values):
    connection = connect()
    print(values)
    vq = "("
    for val in values:
        vq = vq + "\'" + val + "\',"
    vq = vq[:-1]
    vq = vq + ")"
    query = "SELECT question, category from Questions where category in " + vq + " ORDER BY RAND() LIMIT 5;"
    onnection = connect()
    cursor = connection.cursor()
    # print(query)
    cursor.execute(query)
    qsns = cursor.fetchall()

    connection.close()
    return_list = list()
    for qsn in qsns:
        return_list.append({"question": qsn[0], "category": qsn[1]})

    return return_list

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

def get_answer(question):
    #
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT answer FROM Questions WHERE question ='"+question+"';")
    value = cursor.fetchone()
    connection.close()
    try:
        return value[0]
    except:
        return 0

def save_profile(fn, email, pwd, resume):
    try:
        # print(idno)
        connection = connect()
        cursor = connection.cursor()
        insertStatement = INSERT_BASIC_DETAILS.format(fn=fn, email=email, pwd=pwd, resume_path=resume)
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
        # print(ke)
        return False
    except:
        return False


def save_user_qsn_answer():
    pass
