import boto3
from PIL import Image

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

    # Upload a new file
#data = open('test.jpg', 'rb')
#s3.Bucket('kdebro-473-final-project').put_object(Key='test.jpg', Body=data)
img = Image.open("test.jpg")
img.show()