import os
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "scien-z"
AWS_S3_ENDPOINT_URL = "https://scien-z-ul2t7.ondigitalocean.app"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
AWS_LOCATION = "https://scien-z.ams3.digitaloceanspaces.com"
DEFAULT_FILE_STORAGE = "scien-z.cdn.backends.MediaRootS3BotoStorage"
