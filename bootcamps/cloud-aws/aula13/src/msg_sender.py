import boto3
from dotenv import load_dotenv
import os

load_dotenv()

SQS_QUEUE_URL = os.getenv('SQS_QUEUE_URL')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION_NAME = os.getenv('AWS_REGION_NAME')

sqs = boto3.client(
    'sqs',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION_NAME,
)

try:
    response = sqs.send_message(
        QueueUrl=SQS_QUEUE_URL,
        MessageBody='Mensagem via boto3 aula 13 bootcamp AWS Jornada de Dados'
    )
except Exception as e:
    print('Error trying to send message: {e}')