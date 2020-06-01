import sys
import time

for i in range(5):
    sys.stdout.write('开始训练 {}\n'.format(i))
    sys.stdout.flush()


for i in range(5):
    sys.stderr.write('测试训练错误的情况 {}\n'.format(i))
    sys.stderr.flush()

