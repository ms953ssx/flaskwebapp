FROM python:3.8-slim-buster

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV FLASK_APP="project"
ENV FLASK_DEBUG="1"

# Install dependencies:
COPY . .
RUN pip install -r requirements.txt

EXPOSE 80/tcp
EXPOSE 443/tcp


# Run the application:
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]

