from mrq.task import Task


class Hello(Task):
    def run(self, params):
        print("This is the example task")
        print(type(params))
        return params
