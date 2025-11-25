# GCP Deployment Guide for Soundverse Play API

This guide details how to containerize and deploy the Soundverse Play API to Google Cloud Platform (GCP) using Cloud Run.

## Prerequisites

1.  **GCP Account**: A Google Cloud Platform account.
2.  **gcloud CLI**: Installed and authenticated (`gcloud auth login`).
3.  **Docker**: Installed locally.

## 1. Containerization

The application is already containerized using the provided `Dockerfile`. It uses a multi-stage build for a smaller image size and runs as a non-root user for security.

## 2. GCP Setup

### Set Project and Region
```bash
export PROJECT_ID="siddhant-gond-project"
export REGION="us-central1"

gcloud config set project $PROJECT_ID
```

### Enable APIs
Enable the necessary Google Cloud APIs:
```bash
gcloud services enable artifactregistry.googleapis.com run.googleapis.com cloudbuild.googleapis.com
```

### Create Artifact Registry
Create a Docker repository to store your images:
```bash
gcloud artifacts repositories create soundverse-repo \
    --repository-format=docker \
    --location=$REGION \
    --description="Soundverse Backend Repository"
```

## 3. Build and Push Image

Submit a build to Cloud Build (this builds the image in the cloud and pushes it to Artifact Registry):

```bash
gcloud builds submit --tag $REGION-docker.pkg.dev/$PROJECT_ID/soundverse-repo/soundverse-api:v1 .
```

## 4. Deploy to Cloud Run

Deploy the image to Cloud Run. Replace `YOUR_DB_URL` with your actual PostgreSQL connection string (e.g., from Cloud SQL or Supabase).

```bash
gcloud run deploy soundverse-api \
    --image $REGION-docker.pkg.dev/$PROJECT_ID/soundverse-repo/soundverse-api:v1 \
    --region $REGION \
    --platform managed \
    --allow-unauthenticated \
    --set-env-vars DATABASE_URL="YOUR_DB_URL",PROJECT_NAME="Soundverse Play API"
```

### Notes on Database
For a production setup, it is recommended to use **Cloud SQL**.
1.  Create a Cloud SQL instance (PostgreSQL).
2.  Create a database and user.
3.  Connect Cloud Run to Cloud SQL using the `--add-cloudsql-instances` flag.

## 5. Verification

After deployment, Cloud Run will provide a URL (e.g., `https://soundverse-api-xyz.a.run.app`).

1.  **Frontend**: Open the URL in your browser. You should see the Soundverse Play interface.
2.  **API Docs**: Visit `/docs` (e.g., `https://.../docs`) to see the Swagger UI.
3.  **Health Check**: Visit `/health` to confirm the service is running.

## 6. CI/CD (Optional)

You can set up a Cloud Build trigger to automatically build and deploy whenever you push to GitHub.
