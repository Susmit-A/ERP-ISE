from .FirebaseObject import FirebaseObject


class Student(FirebaseObject):

    def __init__(self, usn=None, **kwargs):
        super().__init__()
        self.ref = FirebaseObject.reference()
        self.usn = usn
        if usn is not None:
            if len(kwargs.keys()) == 0:
                data = self.ref.child('Student').child(usn).get()

                self.FirstName = data['FirstName']
                self.LastName = data['LastName']
                self.DOB = data['DOB']
                self.Dept = data['Dept']
                self.Semester = data['Semester']
                self.Scheme = data['Scheme']
                self.Subjects = list(data['Subjects'])

            else:
                self.FirstName = kwargs['FirstName']
                self.LastName = kwargs['LastName']
                self.DOB = kwargs['DOB']
                self.Dept = kwargs['Dept']
                self.Semester = kwargs['Semester']
                self.Scheme = kwargs['Scheme']
                self.Subjects = list(kwargs['Subjects'])

        else:
            self.usn = self.FirstName = self.LastName = self.DOB = self.Dept = self.Semester = self.Scheme = ' '
            self.Subjects = []

    def __str__(self):
        return 'USN: ' + self.usn \
                + '\nName: ' + self.FirstName + ' ' + self.LastName \
                + '\nSubjects: ' + str(self.Subjects)

    def upload(self):
        temp = {}
        for i in range(len(self.Subjects)):
            temp[str(i)] = self.Subjects[i]

        self.Subjects = temp
        usn = self.usn
        data = vars(self)
        data.pop('usn')
        data.pop('ref')
        self.ref.child('Student').child(usn).set(data)

    @staticmethod
    def fetch_all(dept=None, sem=None):
        if dept is None and sem is None:
            return FirebaseObject().reference().child('Student').get()

        elif dept is not None and sem is not None:
            retlist = []
            students = FirebaseObject().reference().child('Student').get()
            for key in students.keys():
                student = students[key]
                if student['Dept'] == dept and student['Semester'] == sem:
                    retlist.append((key, student))

            return retlist

        elif dept is not None:
            retlist = []
            students = FirebaseObject().reference().child('Student').get()
            for key in students.keys():
                student = students[key]
                if student['Dept'] == dept:
                    retlist.append((key, student))

            return retlist

        elif sem is not None:
            retlist = []
            students = FirebaseObject().reference().child('Student').get()
            for key in students.keys():
                student = students[key]
                if student['Semester'] == sem:
                    retlist.append((key, student))

            return retlist
