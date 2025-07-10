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

response = sqs.receive_message(
    QueueUrl=SQS_QUEUE_URL,
    MaxNumberOfMessages=10,  # Número máximo de mensagens a receber
    WaitTimeSeconds=10       # Tempo máximo de espera (em segundos)
)

if 'Messages' in response:
    for message in response['Messages']:
        print(f'Mensagem recebida: {message['Body']}')

        # Excluindo a mensagem da fila após o processamento
        sqs.delete_message(
            QueueUrl=SQS_QUEUE_URL,
            ReceiptHandle=message['ReceiptHandle']
        )
        print(f"Mensagem excluída: ID {message['MessageId']}")
else:
    print("Nenhuma mensagem disponível na fila.")

