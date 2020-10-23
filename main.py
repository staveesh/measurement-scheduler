from TaskNode import TaskNode
from DOSDScheduler import DOSDScheduler
from Visualizer import Visualizer

if __name__ == '__main__':
    n = int(input('Enter number of jobs : '))
    jobs = []
    for i in range(n):
        label, arrival_time, execution_time, period = map(int, input('Enter label, arrival_time, execution_time, '
                                                                     'period of job {} : '.format(i+1))
            .strip().split())
        node = TaskNode(label, arrival_time, execution_time, period)
        jobs.append(node)
    m = int(input('Enter number of conflicts : '))
    conflicts = []
    for i in range(m):
        u, v = map(int, input('Enter conflict {} : '.format(i+1)).strip().split())
        conflicts.append((u,v))
    scheduler = DOSDScheduler(jobs, conflicts)
    schedule = scheduler.generate_schedule()
    print(schedule)