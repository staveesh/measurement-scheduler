from ConflictGraph import ConflictGraph
from Visualizer import Visualizer
from TaskNode import TaskNode

import functools as ft


def hcf(a, b):
    if b > a:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // hcf(a, b)


class DOSDScheduler:

    def __init__(self, jobs, conflicts):
        self.jobs = jobs
        self.conflicts = conflicts
        self.job_queue = {}

        periods = [node.get_period() for node in jobs]
        self.hyperperiod = ft.reduce(lcm, periods)

    def get_available_jobs(self, time_instance):
        """
        :param time_instance: a point in time
        :return: jobs available for execution at the given time instance
        """
        available_jobs = []
        for node in self.jobs:
            if (time_instance - node.get_arrival_time()) % node.get_period() == 0:
                available_jobs.append(node)
        return available_jobs

    def build_conflict_graph(self):
        visualizer = Visualizer()
        graph = ConflictGraph()
        for label in self.job_queue:
            graph.add_node(self.job_queue[label])
        for u, v in self.conflicts:
            # Add an edge only if both jobs are in queue
            if u in self.job_queue and v in self.job_queue:
                deg_u = self.job_queue[u].get_degree()
                deg_v = self.job_queue[v].get_degree()
                self.job_queue[u].set_degree(deg_u + 1)
                self.job_queue[v].set_degree(deg_v + 1)
                self.job_queue[u].add_neighbor(self.job_queue[v])
                self.job_queue[v].add_neighbor(self.job_queue[u])
        # visualizer.visualize(graph)

    def generate_schedule(self):
        print('HyperPeriod for the given jobs : {}'.format(self.hyperperiod))
        time = 0
        schedule = []
        while time < self.hyperperiod:
            print('time = {}'.format(time))
            available_jobs = self.get_available_jobs(time)
            print('Jobs available for execution = {}'.format(available_jobs))
            for job in available_jobs:
                label = job.get_label()
                # Remove old instance if it exists
                removed_instance = self.job_queue.pop(label, None)
                if removed_instance:
                    print('Removed expired instance : {}'.format(removed_instance))
                self.job_queue[label] = job
                print('Added {} to the job queue'.format(job))

            # Build conflict graph from job queue
            self.build_conflict_graph()

            job_list = [self.job_queue[key] for key in self.job_queue]
            job_list.sort(key=lambda x: x.degree, reverse=True)
            all_colors = set(range(time+1, self.hyperperiod+1))
            max_color_assigned = -1
            for job in job_list:
                print('Scheduling job : {}'.format(job.get_label()))
                available_colors = all_colors.copy()
                # Find conflicting colors
                conflicting_colors = set()
                for neighbor in job.get_neighbors():
                    conflicting_colors = conflicting_colors.union(neighbor.get_colors())
                print('Conflicting colors : {}'.format(conflicting_colors))
                # Find available colors range
                available_colors = available_colors.intersection(all_colors - conflicting_colors)
                print('Available colors : {}'.format(available_colors))
                # Check if consecutive sequence exists in available_colors
                # the consecutive sequence should be of length equal to
                # the execution time of job
                available_colors_list = list(available_colors)
                prev = available_colors_list[0]
                cur_len = 1
                max_len = 0
                max_color = -1
                print('Finding consecutive colors in available colors...')
                for i in range(1, len(available_colors_list)):
                    max_len = max(cur_len, max_len)
                    if max_len == job.get_execution_time():
                        max_color = available_colors_list[i-1]
                        break
                    if available_colors_list[i] == prev+1:
                        cur_len += 1
                    else:
                        cur_len = 1
                    prev = available_colors_list[i]
                start_time = max_color-job.get_execution_time()
                assigned_colors = set(range(start_time+1, max_color+1))
                job.set_colors(assigned_colors)
                print('Job : {} scheduled successfully at {}, assigned_colors = {}'.format(job.get_label(), start_time+1, assigned_colors))
                schedule.append((job, start_time))
                # Update the arrival time of the job for next run
                completed_job = self.job_queue.pop(job.get_label(), None)
                new_job = TaskNode(completed_job.get_label(),
                                   completed_job.get_arrival_time()+completed_job.get_period(),
                                   completed_job.get_execution_time(),
                                   completed_job.get_period())
                self.jobs.remove(completed_job)
                self.jobs.append(new_job)

                max_color_assigned = max(max_color_assigned, max_color)
            time += max(1, max_color_assigned)
        return schedule
