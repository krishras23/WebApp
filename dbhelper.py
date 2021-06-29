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
            print(create_task_query)
            val = (the_task_name, the_task_importance, the_task_owner)
            with connection.cursor() as cursor:
                cursor.execute(create_task_query, val)
                connection.commit()
                return
    except Error as e:
        print(e)


def update_task(old_owner, new_owner):
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            update_task_query = "UPDATE trello.tasks SET owner = \"" + new_owner + "\" WHERE owner like \"" + old_owner + "\""
            print(update_task_query)
            with connection.cursor() as cursor:
                cursor.execute(update_task_query)
                connection.commit()
                return ""
    except Error as e:
        print(e)


def delete_task(importance):
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            delete_task_query = "delete from trello.tasks where importance = " + str(importance)
            with connection.cursor() as cursor:
                cursor.execute(delete_task_query)
                connection.commit()
                return ""
    except Error as e:
        print(e)


def delete_task_string(importance):
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            delete_task_query = "delete from trello.tasks where importance = {}".format(importance)
            with connection.cursor() as cursor:
                cursor.execute(delete_task_query)
                connection.commit()
                return ""
    except Error as e:
        print(e)


def joining_tables():
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            join_task_query = "join on from trello.tasks where importance = {}".format(importance)
            with connection.cursor() as cursor:
                cursor.execute(join_task_query)
                connection.commit()
                return ""
    except Error as e:
        print(e)

print("reutrn null")

def update(old_owner, new_owner):
    # print("UPDATE trello.tasks SET owner = " + old_owner + " WHERE owner like " + new_owner)
    print("UPDATE trello.tasks SET owner = \"" + old_owner + "\" WHERE owner like \"" + new_owner + "\"")

