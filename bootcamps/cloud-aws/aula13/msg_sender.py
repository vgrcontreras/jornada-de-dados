import boto3
from dotenv import load_dotenv
import os

load_dotenv()

SQS_URL = os.getenv('SQS_URL')

sqs = boto3.client('sqs')

response = sqs.create_queue(
    QueueName='boto3-client-sqs-queue'
)
