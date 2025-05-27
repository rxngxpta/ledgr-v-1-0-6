# Use the official Python 3.13 slim-bookworm image as a base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY ./requirements.txt .

# Install the Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the app directory to the container
COPY . .

# Expose port 8501 for Streamlit
EXPOSE 8080

# Define the command to run the Streamlit app
CMD ["streamlit", "run", "Home.py"]