# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define the command to run the Python script
CMD ["python", "create_pull_request.py", "owner", "repo", "base", "head", "title", "body"]

# Replace "owner", "repo", "base", "head", "title", and "body" with the appropriate default values for your pull request
