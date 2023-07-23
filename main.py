import boto3

# Replace these values with your AWS credentials and region
aws_access_key_id = "YOUR_AWS_ACCESS_KEY"
aws_secret_access_key = "YOUR_AWS_SECRET_KEY"
region_name = "YOUR_AWS_REGION"

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Create an S3 client
s3_client = session.client("s3")

# List all S3 buckets
response = s3_client.list_buckets()
buckets = response["Buckets"]
print("List of S3 Buckets:")
for bucket in buckets:
    print(bucket["Name"])

# Upload a file to S3 bucket
bucket_name = "your-bucket-name"
file_path = "path/to/your/file.txt"
object_key = "file.txt"

try:
    s3_client.upload_file(file_path, bucket_name, object_key)
    print(f"File '{object_key}' uploaded successfully to bucket '{bucket_name}'")
except Exception as e:
    print(f"Error uploading file: {e}")
Replace YOUR_AWS_ACCESS_KEY, YOUR_AWS_SECRET_KEY, and YOUR_AWS_REGION with your actual AWS credentials and region. Also, update your-bucket-name, path/to/your/file.txt, and file.txt with your S3 bucket name, local file path, and the desired object key (file name) to be used in the S3 bucket.

Remember to ensure that the AWS credentials you provide have the necessary permissions to perform the actions you want (e.g., read, write, delete objects in S3). For security reasons, avoid hardcoding the credentials in your script and instead use IAM roles or environment variables to store them securely.





