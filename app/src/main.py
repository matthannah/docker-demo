import os
import pika

def callback(ch, method, properties, body):
    # Print what you get, epic app
    print("Received message: %s" % body)

# Get an env variable
name = os.environ['APP_NAME']
print("%s is starting..." % name)

# Connect to rabbit-mq, notice that docker made the hostname for us :D
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit-mq'))
print("Connected to rabbit-mq")

channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume(callback, queue='hello', no_ack=True)

print("Done!")

# Loop forever! docker won't end the container since our process will be running..
# print('Waiting for messages...')
# channel.start_consuming()
