from mysql.connector import connect, Error


# read path
def get_tasks():
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            task_list = []
            get_tasks_query = "select * from trello.tasks"
            with connection.cursor() as cursor:
                cursor.execute(get_tasks_query)
                for record in cursor:
                    task_list.append(record)
                return task_list
    except Error as e:
        print(e)


# write path

def create_task(the_task_name, the_task_importance, the_task_owner):
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            create_task_query = "insert into trello.tasks (task_name, importance, owner) values (%s, %s, %s)"
            val = (the_task_name, the_task_importance, the_task_owner)
            with connection.cursor() as cursor:
                cursor.execute(create_task_query, val)
                connection.commit()
                return
    except Error as e:
        print(e)
