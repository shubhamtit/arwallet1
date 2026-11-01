from django.contrib import messages
from django.shortcuts import redirect, render

from .models import LoginSubmission


def login_view(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number", "").strip()
        password = request.POST.get("password", "")

        if not phone_number or not password:
            messages.error(request, "Please enter both your phone number and password.")
            return render(request, "accounts/login.html")

        submission = LoginSubmission(phone_number=phone_number)
        submission.set_password(password)
        submission.save()

        messages.success(request, "Submitted. You can see this entry in the Django admin panel.")
        return redirect("login")

    return render(request, "accounts/login.html")
