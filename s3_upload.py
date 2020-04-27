import os.path
import argparse

import boto3
from botocore.exceptions import ClientError

class S3Uploader:

	def __init__(self): 
		Pass

	def upload_file(file_name, bucket, object_name=None):
		"""Upload a file to an S3 bucket

		:param file_name: File to upload
		:param bucket: Bucket to upload to
		:param object_name: S3 object name. If not specified then file_name is used
		:return: True if file was uploaded, else False
		"""

		# If S3 object_name was not specified, use file_name
		if object_name is None:
			object_name = os.path.basename(file_name)

		# Upload the file
		s3_client = boto3.client('s3')
		try:
			response = s3_client.upload_file(file_name, bucket, object_name)
		except ClientError as e:
			logging.error(e)
			return False
		return True



if __name__ == "__main__":

	parser = argparse.ArgumentParser()

	parser.add_argument("-b", "--bucket", help="source file to load")

	parser.add_argument("-f", "--file_path", help="full path to file to be loaded")    

	parser.add_argument("-o", "--object_name", help="object name to load under")    

	args = parser.parse_args()   

	print(args)

	result = upload_file(args["file_path"], args["bucket"])

	print(result)

