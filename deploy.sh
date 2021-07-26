#!bin/bash
gcloud functions deploy ea-job \
    --project=ea-jobs \
    --trigger-topic ea-job \
    --memory=256MB \
    --env-vars-file .env.yaml \
    --region=us-central1 \
    --runtime python39 \
    --entry-point=post_tweet