# Disaster Recovery Solution on GCP - Setup Guide  

### Step 1: Setup Environment  
- Create a GCP project and enable Compute Engine, Cloud Storage, and DNS API.  
- Install Terraform and GCP SDK on your local machine.  

### Step 2: Deploy Infrastructure  
- Run `gcloud deployment-manager deployments create dr-solution --config deployment/deployment-manager.yaml`  
- Or, if using Terraform:  
