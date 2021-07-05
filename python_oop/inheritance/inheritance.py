import math
class Teacher:
    def ask_question(self):
        print('Teacher: do you know area of circle when radios is 10')

class Students(Teacher):
    def answered(self):
        ob = FormulaOfGeometry()
        area = ob.area_of_circle(10)
        print('Students: yes sir I know area is =',area)


class FormulaOfGeometry:
    def area_of_circle(self,radious):
        return math.pi * radious * radious

obj = Students()
obj.ask_question()
obj.answered()

