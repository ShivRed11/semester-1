# Reference solution (rewritten after original work was lost)

# Week 1.5, Session 1: Task 1
#
# The task asks for two lists (to go in Student.md):
#
# Attributes (the STATE of a student - data each object stores):
#   - name          (str)
#   - student_id    (str), e.g. "201234567"
#   - programme     (str), e.g. "BSc Computer Science"
#   - year          (int), year of study
#   - modules       (list of str), modules the student is taking
#   - marks         (dict: module -> int), marks gained so far
#
# Behaviour (METHODS - what a student can do / what we can ask of one),
# chosen to fit the attributes above:
#   - enrol(module)             add a module to the student's list
#   - withdraw(module)          remove a module
#   - record_mark(module, mark) store a mark for a module
#   - average_mark()            mean of all recorded marks
#   - progress()                move on to the next year of study
#
# Below is a small class sketch showing those ideas in code.


class Student:
    """
    A university student.
    """

    def __init__(self, name, student_id, programme, year=1):
        """
        Creates a Student with a name, ID, programme and year of study.
        """
        self.name = name
        self.student_id = student_id
        self.programme = programme
        self.year = year
        self.modules = []
        self.marks = {}

    def enrol(self, module):
        """
        Adds a module to this Student's list of modules.
        """
        if module not in self.modules:
            self.modules.append(module)

    def withdraw(self, module):
        """
        Removes a module from this Student's list of modules.
        """
        if module in self.modules:
            self.modules.remove(module)

    def record_mark(self, module, mark):
        """
        Records a mark for one of this Student's modules.
        """
        self.marks[module] = mark

    def average_mark(self):
        """
        Returns the mean of this Student's marks, or None if there are none.
        """
        if len(self.marks) == 0:
            return None
        return sum(self.marks.values()) / len(self.marks)

    def progress(self):
        """
        Moves this Student on to the next year of study.
        """
        self.year += 1


# Demo
s = Student("Ada", "201234567", "BSc Computer Science")
s.enrol("COMP1850")
s.enrol("COMP1721")
s.record_mark("COMP1850", 72)
s.record_mark("COMP1721", 65)
print(s.name, s.modules, s.average_mark())   # Ada ['COMP1850', 'COMP1721'] 68.5
s.progress()
print(f"Now in year {s.year}")               # Now in year 2
