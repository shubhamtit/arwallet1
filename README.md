# Login Page (Django, learning project)

Single-page mobile login screen (phone number + password). Every submit is
saved and visible in the Django admin.

## Run it

```bash
pip install django
cd loginsite
python manage.py migrate
python manage.py createsuperuser   # for the admin panel
python manage.py runserver
```

- Login page: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## What's in the admin

Under **Accounts > Login submissions** you'll see every phone number, the
submission time, and the password **hash**.

## About the password hash

The password is run through Django's `make_password()` before saving, so the
database never holds the raw text — only a one-way hash. That's the standard,
correct way to handle passwords in any Django app, including a learning one.
You can still see that a submission happened and compare/reset it; you just
can't read the original characters back out of the hash (by design — that's
what makes hashing useful at all). If you ever want to actually log users
back in and verify their password, use `submission.check_password(raw)`.

## Files

- `config/` — project settings/urls
- `accounts/models.py` — the `LoginSubmission` model
- `accounts/views.py` — handles the form POST
- `accounts/admin.py` — admin panel registration
- `accounts/templates/accounts/login.html` — the page itself
