import pymysql
import time
from datetime import datetime
from data_manager.model.task import Task
from data_manager.model.custom_log import CustomLog
from DBUtils.PooledDB import PooledDB, SharedDBConnection


class Db:
    def __init__(self):
        self.pool = PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            maxconnections=12,  # 连接池允许的最大连接数，0和None表示不限制连接数
            mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
            maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
            maxshared=3,
            # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的
            # threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
            setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
            ping=0,
            # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested,
            # 2 = when a cursor is created, 4 = when a query is executed, 7 = always
            host='127.0.0.1',
            port=3306,
            user='root',
            password='root',
            charset='utf8'
        )
        conn = self.pool.connection()
        # self.db = pymysql.connect("localhost", "root", "root", cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print("Database version : %s " % data)

    def __del__(self):
        # self.db.close()
        self.pool.close()

    def get_conn(self):
        conn = self.pool.connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        return conn, cursor

    def close_conn(self, conn, cursor):
        conn.close()
        cursor.close()

    def add_task(self, task):
        sql = """insert into cecl.task(name, create_time, union_train, edgenodes, file, status) 
        values (%s, %s, %s, %s, %s, %s)"""
        conn, cursor = self.get_conn()
        try:
            cursor.execute(
                sql,
                args=(
                    task.name,
                    datetime.fromtimestamp(task.create_time),
                    task.union_train,
                    task.edgenodes,
                    task.file,
                    task.status
                ))
            conn.commit()
            sql = """select max(id) as id from cecl.task"""
            cursor.execute(sql)
            return cursor.fetchone()
        except ValueError as e:
            print(e)
            conn.rollback()

    def start_task(self, task: Task):
        sql = """update cecl.task set start_time = %s, status = %s where id = %s"""
        conn, cursor = self.get_conn()
        try:
            cursor.execute(
                sql,
                args=(
                    datetime.fromtimestamp(task.start_time),
                    1,
                    task.task_id,
                )
            )
            conn.commit()
        except ValueError as e:
            print(e)
            conn.rollback()

    def stop_task(self, task: Task):
        sql = """update cecl.task set end_time = %s, status = %s where id = %s"""
        conn, cursor = self.get_conn()
        try:
            cursor.execute(
                sql,
                args=(
                    datetime.fromtimestamp(task.end_time),
                    2,
                    task.task_id,
                ))
            conn.commit()
        except ValueError as e:
            print(e)
            conn.rollback()

    def finish_task(self, task: Task):
        sql = """update cecl.task set end_time = %s, status = %s where id = %s"""
        conn, cursor = self.get_conn()
        try:
            cursor.execute(
                sql,
                args=(
                    datetime.fromtimestamp(task.end_time),
                    3,
                    task.task_id,
                ))
            conn.commit()
            print("set task:{} finished!".format(task.task_id))
        except ValueError as e:
            print(e)
            conn.rollback()

    def get_all_tasks(self):
        sql = """select id, name,
        unix_timestamp(create_time) as create_time, 
        unix_timestamp(start_time) as start_time, 
        unix_timestamp(end_time) as end_time, 
        union_train, edgenodes, file, status from cecl.task order by id desc"""
        conn, cursor = self.get_conn()
        try:
            cursor.execute(sql)
            return list(cursor.fetchall())
        except ValueError as e:
            print(e)

    def get_task(self, task_id):
        sql = """select * from cecl.task where id = %s"""
        conn, cursor = self.get_conn()
        try:
            cursor.execute(
                sql,
                args=(
                    task_id
                ))
            return cursor.fetchall()
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
        conn, cursor = self.get_conn()
        try:
            cursor.execute(
                sql,
                args=(
                    task.name,
                    task.union_train,
                    task.edgenodes,
                    task.file,
                    task.status,
                    task.task_id,
                ))
            conn.commit()
        except ValueError as e:
            print(e)
            conn.rollback()

    def add_custom_log(self, task_log: CustomLog):
        sql = """insert into cecl.task_log(task_id, content, time) 
        values (%s, %s, %s)"""
        conn, cursor = self.get_conn()
        try:
            cursor.execute(
                sql,
                args=(
                    task_log.task_id,
                    task_log.content,
                    datetime.fromtimestamp(task_log.time),
                ))
            conn.commit()
        except ValueError as e:
            print(e)
            conn.rollback()

    def get_task_log(self, task_id):
        sql = """select id, task_id, content, unix_timestamp(time) as time from cecl.task_log where task_id = %s"""
        conn, cursor = self.get_conn()
        try:
            cursor.execute(
                sql,
                args=(
                    task_id
                ))
            return cursor.fetchall()
        except ValueError as e:
            print(e)


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

    # log = CustomLog(
    #     task_id=1,
    #     content='Test!!',
    #     time=int(time.time())
    # )
    # db.add_custom_log(log)
    print(db.get_task_log(52))
