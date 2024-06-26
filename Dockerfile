# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY cti-backend/requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the contents of the cti-backend directory into the container at /app
COPY cti-backend/ /app/

# Expose port 8000 to allow communication to/from the container
EXPOSE 8000

# Run Django development server when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
