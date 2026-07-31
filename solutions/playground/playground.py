class MyTestClass:

        list_of_instances = []

        def __init__(self, name:str):
                self.name = name
                MyTestClass.list_of_instances.append(self)

        @classmethod
        def list_instances(cls) -> int:
                return len(MyTestClass.list_of_instances)
        


if __name__ == '__main__':

        test1 = MyTestClass('test1')
        test2 = MyTestClass('test2')

        print(len(MyTestClass.list_of_instances))
        print(MyTestClass.list_instances())