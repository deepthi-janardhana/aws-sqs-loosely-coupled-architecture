# aws-sqs-loosely-coupled-architecture
Implementing Loosely Coupled Architecture Using AWS SQS


# Implementing Loosely Coupled Architecture Using AWS SQS

**Objective**  
Improve application reliability and fault tolerance by decoupling the customer-facing application from backend services using a message queue.

**Tools & Technology**  
- AWS Cloud  
- Amazon SQS  
- Amazon EC2  
- AWS IAM  
- Amazon RDS  
- Virtual Machines
- ## Architecture Overview
- Customer Web App  →  Amazon SQS Queue  →  Backend App  →  Amazon RDS
(Producer)         (Buffer)          (Consumer)      (Database)

- The Customer Web Application sends messages to the SQS queue  
- The Backend Application polls the queue and processes the messages  
- After processing, the Backend updates the RDS database  
- IAM provides secure access to all resources  

---## Process Followed (AWS Console)

1. Created an Amazon SQS Standard Queue  
2. Deployed Customer Web Application on EC2  
3. Deployed Backend Application on another EC2  
4. Configured the Web App to send messages to SQS  
5. Configured the Backend to poll messages from SQS  
6. Connected Backend to Amazon RDS  
7. Created IAM roles and policies for secure access  

---

## Sample Code Provided

| Folder     | File                  | Purpose                                      |
|------------|-----------------------|----------------------------------------------|
| `producer/`  | `send_message.py`       | Simulates Customer Web App sending messages  |
| `consumer/`  | `process_messages.py`   | Simulates Backend App polling & processing   |
| `iam/`       | `sqs-policy.json`       | Example IAM policy for SQS access            |

---

## Result / Impact

- Achieved a highly available and loosely coupled architecture  
- Backend failures do not directly affect the customer application  
- Messages are safely buffered in SQS  
- Improved reliability, scalability, and fault tolerance
- 
- ## Note
The actual infrastructure (SQS queue, EC2 instances, IAM roles, and RDS) was configured using the **AWS Management Console**.  
The Python code provided in this repository is a sample demonstration of how the Customer Web Application (Producer) and Backend Application (Consumer) interact with Amazon SQS.

---

---

## Author
Deepthi 
AWS Loosely Coupled Architecture Project
