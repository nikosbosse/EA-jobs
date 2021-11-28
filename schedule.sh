#!bin/bash
gcloud scheduler jobs update pubsub ea-job \
    --project=ea-jobs \
    --schedule="10/30 6-21 * * *" \
    --topic=ea-job \
    --description="Post an EA job offer" \
    --message-body="Post an EA job offer"
