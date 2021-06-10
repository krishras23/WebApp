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
                    db_list.append(db)
                return db_list
    except Error as e:
        print(e)

if __name__ ==  '__main__':
    l = get_databases()
