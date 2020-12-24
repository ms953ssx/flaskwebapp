# FLASK BASED LOGIN SYSTEM


**BEFORE** RUNNING 'docker-compose.yml' OR BUILDING 'Dockerfile' >>
FILL IN EMAIL CREDENTIALS WITHIN '.env.credentials' THEN UNCOMMENT LINE IN '.gitignore' FILE.

Without filling in email credentials, reset password functionality will not work


Reset password functionality currently does not work due to a common issue with flask-mail.Message() method. Changing flask-mail version to 0.9.0 or to latest (0.9.1) has not made a difference.
