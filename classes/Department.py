from .FirebaseObject import FirebaseObject


class Department:
    @staticmethod
    def exists(dept):
        ref = FirebaseObject().reference().child('Department')
        return ref is not None and dept in ref.get().keys() is not None

    @staticmethod
    def fetch_all():
        return FirebaseObject().reference().child('Department').get()

    @staticmethod
    def get_name(code):
        return FirebaseObject.reference().child('Department').get()[code]
