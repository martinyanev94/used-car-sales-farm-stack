# Build the Docker image
docker build -t my-fastapi-app .

# Tag the image for ECR
docker tag my-fastapi-app:latest <your-account-id>.dkr.ecr.<region>.amazonaws.com/my-fastapi-app:latest

# Push the image to ECR
docker push <your-account-id>.dkr.ecr.<region>.amazonaws.com/my-fastapi-app:latest
