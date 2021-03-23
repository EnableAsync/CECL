class Task:
    READY = 0
    RUNNING = 1
    FAIL = 2
    FINISHED = 3
    PULLING = 4
    PULL_FAILURE = 5

    def __init__(self, task_id=0, name='', create_time=0, start_time=0, end_time=0, union_train=0, edge_nodes='',
                 file='', status=0, recent_running_time=0, last_modified_time=0):
        self.task_id = task_id
        self.name = name
        self.create_time = create_time
        self.start_time = start_time
        self.end_time = end_time
        self.union_train = union_train
        self.edge_nodes = edge_nodes
        self.file = file
        self.status = status
        self.recent_running_time = recent_running_time
        self.last_modified_time = last_modified_time



