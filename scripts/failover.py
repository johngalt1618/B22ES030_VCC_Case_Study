from google.cloud import compute_v1

PROJECT_ID = "my-gcp-project"
ZONE = "us-central1-a"
INSTANCE_NAME = "dr-compute-instance"

def start_instance():
    instance_client = compute_v1.InstancesClient()
    operation = instance_client.start(project=PROJECT_ID, zone=ZONE, instance=INSTANCE_NAME)
    print(f"Failover started: {operation.operation_type}")

if __name__ == "__main__":
    start_instance()
