from flask import Flask, request, jsonify
from tinydb import TinyDB, Query
import re

app = Flask(__name__)
db = TinyDB('./app/db.json')


def create_db():
    db.insert({'name': 'MyForm', 'email': 'email', 'phone': 'phone'})


email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
phone_regex = r'^\+7 \d{3} \d{3} \d{2} \d{2}$'
date_regex = r'^\d{2}\.\d{2}\.\d{4}$|^\d{4}-\d{2}-\d{2}$'


def determine_field_type(value):
    if re.match(date_regex, value):
        return 'date'
    elif re.match(phone_regex, value):
        return 'phone'
    elif re.match(email_regex, value):
        return 'email'
    else:
        return 'text'


@app.route('/get_form', methods=['POST'])
def get_form():
    data = request.form
    field_types = {}

    for field_name, value in data.items():
        field_types[field_name] = determine_field_type(value)

    FormTemplate = Query()
    for template in db.all():
        template_fields = {k: v for k, v in template.items() if k != 'name'}

        if all(field in field_types and field_types[field] == template_fields[field] for field in template_fields):
            return jsonify(template['name'])

    return jsonify(field_types)


if __name__ == '__main__':
    create_db()
    app.run(debug=True)
