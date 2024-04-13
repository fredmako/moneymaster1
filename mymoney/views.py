# In views.py

from django.shortcuts import render, redirect
from .forms import SignUpForm
def start(request):
    # View logic for signup start page
    return render(request, 'start.html')
def inner_page(request):
  return render(request,'inner-page.html')
def signup_start(request):
    return render(request,'signupform.html')
def signup_success(request):
    return render (request,'signupsuccess.html')
# views.py

from django.shortcuts import render, redirect
from .forms import SignUpForm  # Import your SignUpForm class from forms.py

def signup_process(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Process valid form data (e.g., save to database)
            form.save()  # Save form data to database or perform other actions
            return redirect('mymoney:signup_success')  # Redirect to success page
        else:
            # Handle invalid form submission (e.g., display errors)
            # You can render the form again with errors to show to the user
            return render(request, 'signupform.html', {'form': form})
    else:
        # Handle GET request (e.g., render initial form)
        form = SignUpForm()  # Create an instance of the SignUpForm
        return render(request, 'signupform.html', {'form': form})