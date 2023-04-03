FROM python:3.9-alpine

# Set the working directory to /fastapi
WORKDIR /fastapi

# Copy the requirements file into the container
COPY requirements.txt .

RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /fastapi
COPY . /fastapi

# Expose port 8001 for the application
EXPOSE 8001

# Run the command to start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]