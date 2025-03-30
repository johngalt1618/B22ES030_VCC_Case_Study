provider "google" {
  project = "my-gcp-project"
  region  = "us-central1"
}

resource "google_compute_instance" "dr_instance" {
  name         = "dr-compute-instance"
  machine_type = "n1-standard-1"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }
}

resource "google_storage_bucket" "dr_backup" {
  name          = "my-dr-backup-bucket"
  location      = "US"
  storage_class = "STANDARD"
}
