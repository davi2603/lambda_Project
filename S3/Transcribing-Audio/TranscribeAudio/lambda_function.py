import boto3

s3 = boto3.client('s3')
transcribe = boto3.client('transcribe')


def lambda_handler(event, context):

    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        object_url = "https://s3.amazonaws.com/{1}/{2}".format(
            source_bucket, key)
        response = transcribe.start_transcription_job(
            TranscriptionJobName=key,
            Media={'MediaFileUri': object_url},
            MediaFormat='mp3',
        )
        print(response)