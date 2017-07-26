FROM python:3.5.2

# Set working directory
RUN mkdir -p /usr/src/app
WORKDIR /user/src/app

# Add requirements (to leverage Docker cache)
ADD ./requirements.txt /user/src/app/requirements.txt

# Install requirements
RUN pip install -r requirements.txt

# Add app
ADD . /user/src/app

# Run server
CMD python manage.py runserver -h 0.0.0.0
