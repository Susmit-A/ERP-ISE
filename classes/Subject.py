from .FirebaseObject import FirebaseObject
import pprint


class Subject(FirebaseObject):
    def __init__(self, code=None, **kwargs):
        super().__init__()
        self.ref = FirebaseObject.reference()
        self.code = code

        if code is not None:
            if (len(kwargs)) == 0:
                data = self.ref.child('Subject').child(code).get()

                self.Name = data['Name']
                self.Branch = data['Branch']
                self.Scheme = data['Scheme']
                self.Semester = data['Semester']

            else:
                self.Name = kwargs['Name']
                self.Branch = kwargs['Branch']
                self.Scheme = kwargs['Scheme']
                self.Semester = kwargs['Semester']

        else:
            self.Name = self.Branch = self.Scheme = self.Semester = self.code = None

    def upload(self):
        code = self.code
        data = vars(self)
        data.pop('code')
        data.pop('ref')
        self.ref.child('Subject').child(code).set(data)
