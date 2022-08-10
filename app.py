import boto3 
import json 

client = boto3.client('secretsmanager')

response = client.put_secret_value(
    SecretId='test003',
    SecretString='{"test003": "thzzzzzzzzzzzzzzzzzzbeen-changed????????"}'
)

print(response)
