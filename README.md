# CECL

## 实体对象定义

### Task

- Python 脚本
- 训练集

## Task 运行流程

1. Client 通过 `POST` 方法传输给 Server 脚本文件和配置文件
2. Server 将脚本文件和训练集封装为 `Task`
3. Server 调用 `Task Runtime` 的 `UploadTask` 方法将 `Task` 传输至 `TaskRuntime`
4. Server 调用 `Task Controller` 的 `AddTask` 方法将已传输完成的 `Task` 添加至调度器
5. `Task Controller` 调用 `Task Runtime` 的 `RunTask` 方法，执行 `Task`
6. `Task Controller` 调用 `Data Manager` 的 `AddTask` 方法，记录执行信息


## Task 信息获取流程

1. Client 向 Server 发出获取信息请求
2. Server 调用 `Task Controller` 的 `GetTaskInfo` 方法获取信息
3. `Task Controller` 调用 `Data Manager` 的 `GetTaskInfo` 方法获取信息
4. Server 返回数据给 Client

## Task 停止流程

1. Client 向 Server 发出停止请求
2. Server 调用 `Task Controller` 的 `StopTask` 停止 Task
3. `Task Controller` 调用 `Data Manager` 的 `StopTaskInfo` 方法记录停止信息
4. Server 返回数据给 Client

## Task 修改流程

1. Client 通过 `POST` 方法传输给 Server 脚本文件和配置文件
2. Server 将脚本文件和训练集封装为 `Task`
3. Server 调用 `Task Runtime` 的 `UploadTask` 方法将 `Task` 传输至 `TaskRuntime`
4. Server 调用 `Task Controller` 的 `StopTask` 停止 Task
4. Server 调用 `Task Controller` 的 `AddTask` 方法将已传输完成的新 `Task` 添加至调度器
5. `Task Controller` 调用 `Task Runtime` 的 `RunTask` 方法，执行 `Task`
6. `Task Controller` 调用 `Data Manager` 的 `AddTask` 方法，记录执行信息