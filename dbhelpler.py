from mysql.connector import connect, Error


def get_databases():
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            # create_db_query = "CREATE DATABASE adventure32"
            # with connection.cursor() as cursor:
            #     cursor.execute(create_db_query)

            db_list = []
            show_db_query = "SHOW DATABASES"
            with connection.cursor() as cursor:
                cursor.execute(show_db_query)
                for db in cursor:
                    print(db[0])
                    db_list.append(db)
                return db_list
    except Error as e:
        print(e)


def get_students():
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            db_list = []
            get_student_query = "select * from test.student"
            with connection.cursor() as cursor:
                cursor.execute(get_student_query)
                print("running query")
                for record in cursor:
                    print(record[0])
                    print(record[1])
                    db_list.append(record)
                return db_list
    except Error as e:
        print(e)


def insert_student(student_name, student_age):
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            create_student_query = "insert into test.student (name, age) values (%s, %s)"
            val = (student_name, student_age)
            with connection.cursor() as cursor:
                cursor.execute(create_student_query, val)
                connection.commit()
                return
    except Error as e:
        print(e)


if __name__ == '__main__':
    insert_student("kapil", 33)
