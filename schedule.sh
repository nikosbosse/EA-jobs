#!bin/bash
gcloud scheduler jobs create pubsub ea-job \
    --project=ea-jobs \
    --schedule="0 6-21/3 * * *" \
    --topic=ea-job \
    --description="Post an EA job offer" \
    --message-body="Post an EA job offer"