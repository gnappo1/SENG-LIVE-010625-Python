from lib.appointment import *


class Doctor:
    all_ = []

    def __init__(self, name, field):
        self.name = name
        self.field = field
        type(self).all_.append(self)
    
    def appointments(self):
        return [appt for appt in Appointment.all_ if self is appt.doctor]

    def patients(self):
        return list({appt.patient for appt in self.appointments()})