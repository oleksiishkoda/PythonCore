class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.fullname = fname + ' ' + lname
        self.email = fname.lower() + '.' + lname.lower() + '@company.com'
