import boto3
import json
from datetime import datetime

# Create SQS client
sqs = boto3.client('sqs', region_name='us-east-1')

# Replace with your actual Queue URL
QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/123456789012/CustomerOrderQueue'

def send_order_message(order_id, customer_name, product, quantity):
    message = {
        "order_id": order_id,
        "customer_name": customer_name,
        "product": product,
        "quantity": quantity,
        "timestamp": str(datetime.now())
    }

    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(message)
    )

    print("Message sent successfully!")
    print("Message ID:", response['MessageId'])

# Example usage
if __name__ == "__main__":
    send_order_message(
        order_id="ORD-1001",
        customer_name="John Doe",
        product="Laptop",
        quantity=1
    )
