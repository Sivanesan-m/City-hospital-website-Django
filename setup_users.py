from django.contrib.auth.models import User
from hospital.models import Doctor, Patient

# Create doctor user
d_user = User.objects.create_user('doctor1', 'doctor@example.com', 'pass')
d = Doctor.objects.create(user=d_user, specialization='Cardiology')

# Create patient user
p_user = User.objects.create_user('patient1', 'patient@example.com', 'pass')
p = Patient.objects.create(user=p_user, age=30)

print("Users created successfully")