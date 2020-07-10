import pymysql
import time
from datetime import datetime
from data_manager.model.task import Task
from data_manager.model.custom_log import CustomLog


class Db:
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "root", cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT VERSION()")
        data = self.cursor.fetchone()
        print("Database version : %s " % data)

    def __del__(self):
        self.db.close()

    def add_task(self, task):
        sql = """insert into cecl.task(name, create_time, union_train, edgenodes, file, status) 
        values (%s, %s, %s, %s, %s, %s)"""
        try:
            self.cursor.execute(
                sql,
                args=(
                    task.name,
                    datetime.fromtimestamp(task.create_time),
                    task.union_train,
                    task.edgenodes,
                    task.file,
                    task.status
                ))
            self.db.commit()
            sql = """select max(id) from cecl.task"""
            self.cursor.execute(sql)
            return self.cursor.fetchone()
        except ValueError as e:
            print(e)
            self.db.rollback()

    def start_task(self, task: Task):
        sql = """update cecl.task set start_time = %s, status = %s where id = %s"""
        try:
            self.cursor.execute(
                sql,
                args=(
                    datetime.fromtimestamp(task.start_time),
                    1,
                    task.task_id,
                )
            )
            self.db.commit()
        except ValueError as e:
            print(e)
            self.db.rollback()

    def stop_task(self, task: Task):
        sql = """update cecl.task set end_time = %s, status = %s where id = %s"""
        try:
            self.cursor.execute(
                sql,
                args=(
                    datetime.fromtimestamp(task.end_time),
                    2,
                    task.task_id,
                ))
            self.db.commit()
        except ValueError as e:
            print(e)
            self.db.rollback()

    def finish_task(self, task: Task):
        sql = """update cecl.task set end_time = %s, status = %s where id = %s"""
        try:
            self.cursor.execute(
                sql,
                args=(
                    datetime.fromtimestamp(task.end_time),
                    3,
                    task.task_id,
                ))
            self.db.commit()
        except ValueError as e:
            print(e)
            self.db.rollback()

    def get_all_tasks(self):
        sql = """select id, name,
        unix_timestamp(create_time) as create_time, 
        unix_timestamp(start_time) as start_time, 
        unix_timestamp(end_time) as end_time, 
        union_train, edgenodes, file, status from cecl.task"""
        try:
            self.cursor.execute(sql)
            return list(self.cursor.fetchall())
        except ValueError as e:
            print(e)

    def get_task(self, task_id):
        sql = """select * from cecl.task where id = %s"""
        try:
            self.cursor.execute(
                sql,
                args=(
                    task_id
                ))
            return self.cursor.fetchall()
        except ValueError as e:
            print(e)

    def update_task(self, task: Task):
        sql = """update cecl.task set 
        name = %s, 
        union_train = %s,
        edgenodes = %s,
        file = %s,
        status = %s
        where id = %s"""

        try:
            self.cursor.execute(
                sql,
                args=(
                    task.name,
                    task.union_train,
                    task.edgenodes,
                    task.file,
                    task.status,
                    task.task_id,
                ))
            self.db.commit()
        except ValueError as e:
            print(e)
            self.db.rollback()

    def add_custom_log(self, task_log: CustomLog):
        sql = """insert into cecl.task_log(task_id, content, time) 
        values (%s, %s, %s)"""
        try:
            self.cursor.execute(
                sql,
                args=(
                    task_log.task_id,
                    task_log.content,
                    datetime.fromtimestamp(task_log.time),
                ))
            self.db.commit()
        except ValueError as e:
            print(e)
            self.db.rollback()


if __name__ == '__main__':
    now = int(time.time())
    now = datetime.fromtimestamp(now)
    db = Db()
    # t = Task(
    #     task_id=1,
    #     name="test_task",
    #     create_time=int(time.time()),
    #     union_train=0,
    #     edgenodes='nodes',
    #     file='train.py'
    # )
    # db.add_task(t)

    log = CustomLog(
        task_id=1,
        content='Test!!',
        time=int(time.time())
    )
    db.add_custom_log(log)
