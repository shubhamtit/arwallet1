from django.contrib import admin

from .models import LoginSubmission


@admin.register(LoginSubmission)
class LoginSubmissionAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "created_at")
    list_filter = ("created_at",)
    search_fields = ("phone_number",)
    readonly_fields = ("phone_number", "password_hash", "created_at")
    ordering = ("-created_at",)
