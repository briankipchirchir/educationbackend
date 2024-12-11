from app import app, db
from app.models import IndividualRegistration, InstitutionRegistration
from faker import Faker
import random

# Create an instance of Faker
fake = Faker()

# Function to seed data
def seed_data():
    with app.app_context():
        # Create fake individual registrations
        for _ in range(10):  # Generate 10 fake individual registrations
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            phone = fake.phone_number()
            selected_dates = [fake.date_this_year() for _ in range(random.randint(1, 3))]  # Random dates in this year

            new_individual = IndividualRegistration(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                selected_dates=selected_dates
            )
            db.session.add(new_individual)

        # Create fake institution registrations
        for _ in range(5):  # Generate 5 fake institution registrations
            institution_name = fake.company()
            institution_address = fake.address()
            phone = fake.phone_number()
            email = fake.email()
            exhibition_choices = [fake.word() for _ in range(random.randint(1, 2))]  # Random exhibition choices

            new_institution = InstitutionRegistration(
                institution_name=institution_name,
                institution_address=institution_address,
                phone=phone,
                email=email,
                exhibition_choices=exhibition_choices
            )
            db.session.add(new_institution)

        # Commit the session to save all the fake data to the database
        db.session.commit()

        print("Fake data has been added to the database!")

# Run the function to seed the data
seed_data()
