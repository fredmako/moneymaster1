from django.shortcuts import render, redirect



from .forms import SignUpForm  # Assuming forms.py is in the app directory

def signup_start(request):
  return render(request, 'start.html')  # Redirect to start template


def signup_process(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      # Process valid form data (e.g., save to model)
      # ...
      return redirect('mymoney:success')  # Use the registered namespace (mymoney)
  # ...


