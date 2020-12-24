FROM python:3.8-slim-buster

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV FLASK_APP="project"
ENV FLASK_DEBUG="1"
ENV MAIL_USERNAME='flaskapp181392@yahoo.com'
ENV MAIL_PASSWORD='&17UKYhQtSw9'

# Install dependencies:
COPY . .
RUN pip install -r requirements.txt

# Run the application:
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
