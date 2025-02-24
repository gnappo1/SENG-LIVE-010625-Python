import datetime


class Appointment:
    all_ = []

    def __init__(self, doctor, patient, reason_for_visit, date):
        self.reason_for_visit = reason_for_visit
        self.date = date
        self.doctor = doctor
        self.patient = patient
        type(self).all_.append(self)

    @property
    def doctor(self):
        return self._doctor

    @doctor.setter
    def doctor(self, doctor):
        if isinstance(doctor, Doctor):
            self._doctor = doctor
        else:
            raise TypeError("Doctor must be a Doctor class instance")

    @property
    def patient(self):
        return self._patient

    @patient.setter
    def patient(self, patient):
        if isinstance(patient, Patient):
            self._patient = patient
        else:
            raise TypeError("patient must be a Patient class instance")

from lib.doctor import Doctor
from lib.patient import Patient
