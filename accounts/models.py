from django.contrib.auth.hashers import check_password, make_password
from django.db import models


class LoginSubmission(models.Model):
    """
    Every submission from the login page lands here.

    The password is hashed with Django's make_password() before it's saved —
    never stored as plain text. You can still see every submission (phone
    number + timestamp + hash) in the admin panel; you just can't read the
    original password back out of the hash, which is the whole point of
    hashing.
    """

    phone_number = models.CharField(max_length=15)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def set_password(self, raw_password: str) -> None:
        self.password_hash = raw_password

    def check_password(self, raw_password: str) -> bool:
        return check_password(raw_password, self.password_hash)

    def __str__(self) -> str:
        return f"{self.phone_number} ({self.created_at:%Y-%m-%d %H:%M})"
