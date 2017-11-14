# Start defining our image from the python alpine image, which itself is defined upon other images!
FROM python:3.4.7-alpine3.4

# Install pika client for RabbitMQ
RUN pip install pika

# Move files from host to container
COPY src/main.py /src/main.py

# Set an environment variable
ENV APP_NAME "Cool test app"

# If we were running a webserver we could expose port 80
# EXPOSE 80

# Run this command when the container launches
CMD ["python", "/src/main.py"]
