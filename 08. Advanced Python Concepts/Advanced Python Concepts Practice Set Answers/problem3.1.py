class MathUtils:
    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod 
    def description(cls):
        print("This is a utility class for math operations.")

# a = MathUtils
# print(a.add(3, 54))
# a.description()

MathUtils.description()
print(MathUtils.add(4, 6))