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


# create connection to update the database

def write_to_db(task_query):
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(task_query)
                connection.commit()
                return ""
    except Error as e:
        print(e)


# write path

def create_task(name, importance, owner):
    create_task_query = "insert into trello.tasks (task_name, importance, owner) " \
                        "values (\"{}\", {}, \"{}\")".format(name, importance, owner)
    write_to_db(create_task_query)


def update_task(new_owner, old_owner):
    update_task_query = "UPDATE trello.tasks SET owner = {} WHERE owner like {}".format(new_owner, old_owner)
    write_to_db(update_task_query)


def delete_task(importance):
    delete_task_query = "delete from trello.tasks where importance = {}".format(importance)
    write_to_db(delete_task_query)
