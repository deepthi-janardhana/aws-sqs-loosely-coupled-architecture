import boto3
import json
import time

# Create SQS client
sqs = boto3.client('sqs', region_name='us-east-1')

# Replace with your actual Queue URL
QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/123456789012/CustomerOrderQueue'

def process_message(message_body):
    order = json.loads(message_body)
    print("Processing Order:")
    print(f"  Order ID   : {order['order_id']}")
    print(f"  Customer   : {order['customer_name']}")
    print(f"  Product    : {order['product']}")
    print(f"  Quantity   : {order['quantity']}")
    print(f"  Timestamp  : {order['timestamp']}")
    print("-" * 40)
    
    # Here you would normally update the RDS database

def poll_queue():
    print("Backend started. Waiting for messages...")
    
    while True:
        response = sqs.receive_message(
            QueueUrl=QUEUE_URL,
            MaxNumberOfMessages=5,
            WaitTimeSeconds=10
        )

        messages = response.get('Messages', [])

        if not messages:
            print("No messages. Waiting...")
            continue

        for message in messages:
            process_message(message['Body'])

            # Delete message after successful processing
            sqs.delete_message(
                QueueUrl=QUEUE_URL,
                ReceiptHandle=message['ReceiptHandle']
            )
            print("Message deleted from queue.\n")

if __name__ == "__main__":
    poll_queue()
