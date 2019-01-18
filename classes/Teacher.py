from .FirebaseObject import FirebaseObject


class Teacher(FirebaseObject):
    def __init__(self, code, **kwargs):
        super().__init__()
        self.ref = FirebaseObject.reference()
        self.code = code

        if code is not None:
            if (len(kwargs)) == 0:
                data = self.ref.child('Teacher').child(code).get()

                self.FirstName = data['FirstName']
                self.LastName = data['LastName']
                self.Designation = data['Designation']
                self.Dept = data['Dept']

            else:
                self.FirstName = kwargs['FirstName']
                self.LastName = kwargs['LastName']
                self.Designation = kwargs['Designation']
                self.Dept = kwargs['Dept']

        else:
            self.FirstName = self.LastName = self.Dept = self.Designation = self.code = None

    def upload(self):
        code = self.code
        data = vars(self)
        data.pop('code')
        data.pop('ref')
        self.ref.child('Teacher').child(code).set(data)

    @staticmethod
    def fetch_all(dept=None):
        if dept is None:
            return FirebaseObject().reference().child('Teacher').get()
        else:
            retlist = []
            teachers = FirebaseObject().reference().child('Teacher').get()
            for code in teachers.keys():
                detail = teachers[code]
                if detail['Dept'] == dept:
                    retlist.append((code, detail))

            return retlist
