from django import forms

class SignUpForm(forms.Form):
  name = forms.CharField(label="Full Name", max_length=100, required=True)
  email = forms.EmailField(label="Email Address", required=True)
  phone = forms.CharField(label="Phone Number", required=True)

  # Add any additional validation or field types as needed
