from dbhelper import write_to_db


def delete_task_string(importance):
    delete_task_query = "delete from trello.tasks where importance = " + str(importance)
    write_to_db(delete_task_query)


def update_task_string(old_owner, new_owner):
    update_task_query = "UPDATE trello.tasks SET owner = \"" + new_owner + "\" WHERE owner like \"" + old_owner + "\""
    write_to_db(update_task_query)


# archive (what did not work)

def read_from_db(task_query):
    try:
        with connect(
                host="localhost",
                user='root',
                password='tomato',
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(task_query)
                result = cursor.fetchall()
                for row in result:
                    print(row)
    except Error as e:
        print(e)


# read path
def get_tasks():
    get_tasks_query = "select * from trello.tasks"
    read_from_db(get_tasks_query)
