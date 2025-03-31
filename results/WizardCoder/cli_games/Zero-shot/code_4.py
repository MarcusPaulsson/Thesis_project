class AssessmentSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade, major):
        student_data = {'name': name, 'grade': grade, 'major': major, 'courses': {}}
        self.students[name] = student_data


    def add_course_score(self, name, course, score):
        if name in self.students:
            self.students[name]['courses'][course] = score


    def get_gpa(self, name):
        if name not in self.students:
            return None
        total_score = 0
        count = 0
        for course, score in self.students[name]['courses'].items():
            if 60 <= score < 100:
                total_score += 4 * score
            elif 90 <= score <= 100:
                total_score += 5 * score
            else:
                total_score += 0
            count += 1
        return None if not count else round(total_score / count, 1)

    def get_all_students_with_fail_course(self):
        fail_list = []
        for student in self.students:
            courses = self.students[student]['courses'].values()
            if any([score < 60 for score in courses]):
                fail_list.append(student)
        return fail_list

    def get_course_average(self, course):
        scores = [self.students[student]['courses'][course] for student in self.students if course in self.students[student]['courses']]
        return sum(scores) / len(scores) if scores else None

    def get_top_student(self):
        max_gpa = 0
        top_student = None
        for student in self.students:
            gpa = self.get_gpa(student)
            if gpa and gpa > max_gpa:
                max_gpa = gpa
                top_student = student
        return top_student