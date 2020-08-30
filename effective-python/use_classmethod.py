import os
import random
from threading import Thread



class InputData:
    def read(self):
      raise NotImplementedError


class GenericInputData:
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
      with open(self.path) as f:
        return f.read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config["data_dir"]
        for name in os.listdir(data_dir):
          yield cls(os.path.join(data_dir, name))


class Worker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


class GenericWorker:
    def ___init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError 

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count("/")

    def reduce(self, other):
        self.result += other.result



def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))

def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers

def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result

def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)

def write_test_files(tmpdir):
    os.makedirs(tmpdir, 777, True)
    for iten in range(100):
        with open(os.path.join(tmpdir, str(iten)), "w") as f:
            f.write("\n" * random.randint(0, 100))


if __name__ == "__main__":
    tmpdir = "test_inputs"
    config = {"data_dir": tmpdir}
    result = mapreduce(LineCountWorker, PathInputData, config)
    print(f"There are {result} lines")
