from flask_restful import Resource


class Person(Resource):
    def get(self):
        return { "patient": { "title": "Patient's Bio", "Bio": { "patientList": { "patient-entry":{ "ID": "PT3222", "Name": "Thirafi wian", "Gender": "Male", "Diagnose": "Influenza", "Recomended Medicine": { "Paracetamol": "For throat", "Painkiller": "Reducing Pain" }, "Date to revisited": ["14/02/2019", "21/02/2019"] } } } } }