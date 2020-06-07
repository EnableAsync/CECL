# CECL

## 文件目录说明

| 目录 | 说明 |
| :------: | :------:
| sql | 数据库定义 |
| data_manager | 数据库服务 |
| message_hub | 消息处理服务 |
| server | Web 服务器 |
| task_controller | Task 调度服务 |
| task_runtime | Task 运行时 |

## 运行说明
1. 执行 `data_manager` 中的 `data_manger_server.py`
2. 执行 `task_runtime` 中的 `task_runtime_server.py`
3. 执行 `task_controller` 中的 `task_controller_server.py`
4. 测试执行 `task_runtime` 中的 `/gen/task_runtime_client.py`


## 实体对象定义

### Task

- Python 脚本
- 训练集

### Task Runtime

- 需要测试

## Task 运行流程

1. Client 通过 `POST` 方法传输给 Server 脚本文件和配置文件
2. Server 将脚本文件和训练集封装为 `Task`
3. Server 调用 `Task Runtime` 的 `UploadTask` 方法将 `Task` 传输至 `TaskRuntime`
4. Server 调用 `Task Controller` 的 `AddTask` 方法将已传输完成的 `Task` 添加至调度器
5. `Task Controller` 调用 `Task Runtime` 的 `StartTask` 方法，执行 `Task`
6. `Task Controller` 调用 `Data Manager` 的 `AddTask` 方法，记录执行信息
7. `Task Runtime` 通过调用 `Task Controller` 的 `AddCustomLogCallback` 方法向 `Data Manager` 添加用户脚本信息

## Task 信息获取流程

1. Client 向 Server 发出获取信息请求
2. Server 调用 `Data Manager` 的 `GetTask` 方法获取历史信息
3. Server 返回数据给 Client

## Task 停止流程

1. Client 向 Server 发出停止请求
2. Server 调用 `Task Controller` 的 `StopTask` 停止 Task
3. `Task Controller` 调用 `Data Manager` 的 `StopTask` 方法记录停止信息
4. Server 返回数据给 Client

## Task 修改流程

1. Client 通过 `POST` 方法传输给 Server 脚本文件和配置文件
2. Server 将脚本文件和训练集封装为 `Task`
3. Server 调用 `Task Runtime` 的 `UploadTask` 方法将 `Task` 传输至 `TaskRuntime`
4. Server 调用 `Task Controller` 的 `StopTask` 停止 Task
4. Server 调用 `Task Controller` 的 `AddTask` 方法将已传输完成的新 `Task` 添加至调度器
5. `Task Controller` 调用 `Task Runtime` 的 `StartTask` 方法，执行 `Task`
6. `Task Controller` 调用 `Data Manager` 的 `AddTask` 方法，记录执行信息

## 联合 Task 运行流程

1. Client 通过 `POST` 方法传输给 Server 脚本文件和配置文件
2. Server 将脚本文件和训练集封装为 `Task`
3. Server 调用 `Message Hub` 的 `SendTask` 方法，通知 `Edge` 从 Server 拉取 `Task`
4. Server 调用 `Task Controller` 的 `AddTask` 方法将已传输完成的 `Task` 添加至调度器
5. `Task Controller` 调用 `Message Hub` 的 `StartTask` 方法，通知 `Edge` 执行 `Task`
6. `Task Controller` 调用 `Data Manager` 的 `AddTask` 方法，记录执行信息

## Task 描述性信息修改

1. Client 通过 `POST` 方法传输给 Server 脚本文件和配置文件
2. Server 将脚本文件和训练集封装为 `Task`
3. `Task Controller` 调用 `Data Manager` 的 `UpdateTask` 方法，更新信息