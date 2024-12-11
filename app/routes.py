from flask import request, jsonify
from app import app, db 
from flask_cors import CORS 
from datetime import datetime
from app.models import IndividualRegistration, InstitutionRegistration,Feedback


CORS(app)

@app.route('/')
def index():
    return "Welcome to the Registration API!"


@app.route('/individuals', methods=['GET'])
def get_individuals():
    individuals = IndividualRegistration.query.all()  
    individuals_list = []
    
    for individual in individuals:
        individuals_list.append({
            'id': individual.id,
            'first_name': individual.first_name,
            'last_name': individual.last_name,
            'email': individual.email,
            'phone': individual.phone,
            'selected_dates': individual.selected_dates,
            'created_at': individual.created_at
        })

    return jsonify(individuals_list)

# GET route to retrieve a specific individual by ID
@app.route('/individuals/<int:id>', methods=['GET'])
def get_individual(id):
    individual = IndividualRegistration.query.get_or_404(id)  # Fetch individual by ID

    return jsonify({
        'id': individual.id,
        'first_name': individual.first_name,
        'last_name': individual.last_name,
        'email': individual.email,
        'phone': individual.phone,
        'selected_dates': individual.selected_dates,
        'created_at': individual.created_at
    })

# GET route to retrieve all institution registrations
@app.route('/institutions', methods=['GET'])
def get_institutions():
    institutions = InstitutionRegistration.query.all()  # Fetch all institution registrations from the database
    institutions_list = []

    for institution in institutions:
        institutions_list.append({
            'id': institution.id,
            'institution_name': institution.institution_name,
            'institution_address': institution.institution_address,
            'phone': institution.phone,
            'email': institution.email,
            'exhibition_choices': institution.exhibition_choices,
            'created_at': institution.created_at
        })

    return jsonify(institutions_list)

# GET route to retrieve a specific institution by ID
@app.route('/institutions/<int:id>', methods=['GET'])
def get_institution(id):
    institution = InstitutionRegistration.query.get_or_404(id)  # Fetch institution by ID

    return jsonify({
        'id': institution.id,
        'institution_name': institution.institution_name,
        'institution_address': institution.institution_address,
        'phone': institution.phone,
        'email': institution.email,
        'exhibition_choices': institution.exhibition_choices,
        'created_at': institution.created_at
    })
@app.route('/register/individual', methods=['POST'])
def register_individual():
    data = request.get_json()

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    phone = data.get('phone')
    selected_dates = data.get('selected_dates')

    # Check if required fields are filled
    if not first_name or not last_name or not email or not phone or not selected_dates:
        return jsonify({"error": "All fields are required"}), 400

    # Remove the email check section, so this part is not executed anymore
    # existing_registration = IndividualRegistration.query.filter_by(email=email).first()
    # if existing_registration:
    #     return jsonify({"error": "Email already registered"}), 400

    # Create a new registration
    new_registration = IndividualRegistration(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        selected_dates=selected_dates  # The array of dates
    )
    
    db.session.add(new_registration)
    db.session.commit()

    return jsonify({"message": "Registration successful"}), 201



@app.route('/register/institution', methods=['POST'])
def register_institution():
    try:
        data = request.get_json()

        # Validate data
        if not data:
            return jsonify({"error": "Invalid request, JSON body is required."}), 400

        institution_name = data.get('institution_name')
        institution_address = data.get('institution_address')
        phone = data.get('phone')
        email = data.get('email')
        exhibition_choices = data.get('exhibition_choices')

        # Log the received data
        print("Received data:", data)

        if not institution_name:
            return jsonify({"error": "Institution name is required."}), 400
        if not institution_address:
            return jsonify({"error": "Institution address is required."}), 400
        if not phone:
            return jsonify({"error": "Phone number is required."}), 400
        if not email:
            return jsonify({"error": "Email is required."}), 400
        if not exhibition_choices or not isinstance(exhibition_choices, list):
            return jsonify({"error": "Exhibition choices must be a non-empty list."}), 400

        # Check if email is already registered
        existing_institution = InstitutionRegistration.query.filter_by(email=email).first()
        if existing_institution:
            return jsonify({"error": "Email already registered"}), 400

        # Create new institution registration
        new_institution = InstitutionRegistration(
            institution_name=institution_name,
            institution_address=institution_address,
            phone=phone,
            email=email,
            exhibition_choices=exhibition_choices
        )

        db.session.add(new_institution)
        db.session.commit()

        return jsonify({"message": "Institution registration successful!"}), 201

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500






# GET route to retrieve all feedback submissions
@app.route('/feedback', methods=['GET'])
def get_feedback():
    feedbacks = Feedback.query.all()  # Fetch all feedbacks from the database
    feedback_list = []
    
    for feedback in feedbacks:
        feedback_list.append({
            'id': feedback.id,
            'name': feedback.name,
            'email': feedback.email,
            'message': feedback.message,
            'created_at': feedback.created_at
        })

    return jsonify(feedback_list)

# GET route to retrieve a specific feedback by ID
@app.route('/feedback/<int:id>', methods=['GET'])
def get_single_feedback(id):
    feedback = Feedback.query.get_or_404(id)  # Fetch feedback by ID

    return jsonify({
        'id': feedback.id,
        'name': feedback.name,
        'email': feedback.email,
        'message': feedback.message,
        'created_at': feedback.created_at
    })

# POST route for submitting feedback
@app.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()

    # Get the form data
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Validate data
    if not name or not email or not message:
        return jsonify({"error": "All fields are required."}), 400

    # Create new feedback entry
    new_feedback = Feedback(
        name=name,
        email=email,
        message=message
    )

    db.session.add(new_feedback)
    db.session.commit()

    return jsonify({"message": "Feedback submitted successfully!"}), 201