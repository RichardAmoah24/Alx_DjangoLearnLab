from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Define a test function that checks the user's role
def is_admin(user):
    # Make sure the user is authenticated and has a profile
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# Apply decorator to restrict access to only Admin users
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')
