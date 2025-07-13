from flask import Blueprint, request, jsonify
from models import KPAForm
from extensions import db

kpa_bp = Blueprint('kpa', __name__)

@kpa_bp.route('/kpa-form', methods=['POST'])
def create_kpa():
    data = request.get_json()
    new_form = KPAForm(
        name=data['name'],
        department=data['department'],
        score=data['score']
    )
    db.session.add(new_form)
    db.session.commit()
    return jsonify({"message": "KPA form created", "id": new_form.id}), 201

@kpa_bp.route('/kpa-forms', methods=['GET'])
def get_kpa_forms():
    forms = KPAForm.query.all()
    return jsonify([
        {"id": f.id, "name": f.name, "department": f.department, "score": f.score}
        for f in forms
    ])
