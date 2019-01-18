from .FirebaseObject import FirebaseObject


class Scheme:
    @staticmethod
    def exists(scheme):
        ref = FirebaseObject().reference().child('Scheme')
        return ref is not None and scheme in ref.get().keys() is not None

    @staticmethod
    def get_years(scheme):
        ref = FirebaseObject().reference().child('Scheme').child(scheme).get()
        return ref.keys()

    @staticmethod
    def scheme_for(year):
        ref = FirebaseObject().reference().child('Scheme')
        schemes = ref.get().keys()
        for scheme in schemes:
            years = ref.child(scheme).get().keys()
            if str(year) in years:
                return scheme

        return None
