class Task:
    def __init__(self, task_id=0, name='', create_time=0, start_time=0, end_time=0, union_train=0, edgenodes='',
                 file='', status=0):
        self.task_id = task_id
        self.name = name
        self.create_time = create_time
        self.start_time = start_time
        self.end_time = end_time
        self.union_train = union_train
        self.edgenodes = edgenodes
        self.file = file
        self.status = status
