import math
from teacher import Teacher
#multilabel inheritance class

class Students(Teacher):
    def answered(self):
        obj = Students()
        print('Students: yes sir I know area is =', super().area_of_circle(10))

obj = Students()
obj.answered()


