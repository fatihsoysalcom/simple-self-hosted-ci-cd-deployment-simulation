import os
import shutil
import datetime

# --- Configuration for our simulated deployment ---
# These settings mimic configuration found in a self-hosted CI/CD tool
# like Jenkins, GitLab CI, or Drone CI.
APP_NAME = "MyWebApp"
BUILD_ARTIFACT_DIR = "build_artifacts" # Directory where build output is placed
DEPLOYMENT_TARGET_DIR = "production_deployments" # Directory where app is deployed

def log_message(message):
    """Logs a timestamped message to the console."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def simulate_build():
    """
    Simulates a build process by creating dummy build artifacts.
    In a real self-hosted CI/CD tool, this would execute build commands
    (e.g., `npm build`, `mvn package`, `go build`).
    """
    log_message(f"Simulating build for {APP_NAME}...")
    if not os.path.exists(BUILD_ARTIFACT_DIR):
        os.makedirs(BUILD_ARTIFACT_DIR)
    with open(os.path.join(BUILD_ARTIFACT_DIR, "index.html"), "w") as f:
        f.write(f"<html><body><h1>Welcome to {APP_NAME}!</h1><p>Deployed on {datetime.datetime.now()}</p></body></html>")
    with open(os.path.join(BUILD_ARTIFACT_DIR, "app.js"), "w") as f:
        f.write("console.log('App started!');")
    log_message(f"Build artifacts created in '{BUILD_ARTIFACT_DIR}'.")

def deploy_application():
    """
    Deploys the application from the build artifacts directory
    to the deployment target directory. This is a core 'automation' step
    that self-hosted developer tools provide for infrastructure management.
    """
    log_message(f"Starting deployment process for {APP_NAME}...")

    # Check if build artifacts exist - a prerequisite for deployment
    if not os.path.exists(BUILD_ARTIFACT_DIR):
        log_message(f"Error: Build artifacts directory '{BUILD_ARTIFACT_DIR}' not found. Please run simulate_build() first.")
        return False

    # Ensure the deployment target directory exists on the 'server'
    if not os.path.exists(DEPLOYMENT_TARGET_DIR):
        log_message(f"Creating deployment target directory: '{DEPLOYMENT_TARGET_DIR}'")
        os.makedirs(DEPLOYMENT_TARGET_DIR)
    else:
        log_message(f"Deployment target directory '{DEPLOYMENT_TARGET_DIR}' already exists.")

    # Clear previous deployment (common practice in CI/CD for clean deployments)
    current_app_path = os.path.join(DEPLOYMENT_TARGET_DIR, APP_NAME)
    if os.path.exists(current_app_path):
        log_message(f"Removing previous deployment at '{current_app_path}'...")
        shutil.rmtree(current_app_path)

    # Copy build artifacts to the deployment target - the actual 'deployment'
    log_message(f"Copying build artifacts from '{BUILD_ARTIFACT_DIR}' to '{current_app_path}'...")
    try:
        shutil.copytree(BUILD_ARTIFACT_DIR, current_app_path)
        log_message(f"Successfully deployed {APP_NAME} to '{current_app_path}'.")
        return True
    except Exception as e:
        log_message(f"Deployment failed: {e}")
        return False

if __name__ == "__main__":
    log_message("--- Simple Self-Hosted CI/CD Deployment Simulation ---")
    log_message("This script simulates an automated deployment step, a core function of")
    log_message("self-hosted developer tools for infrastructure management and automation.")

    # Step 1: Simulate the build process (e.g., by a CI server)
    simulate_build()

    # Step 2: Perform the deployment (e.g., by a CD server or agent)
    if deploy_application():
        log_message(f"Deployment of {APP_NAME} completed successfully.")
        log_message(f"Check the deployed application in the '{DEPLOYMENT_TARGET_DIR}/{APP_NAME}' directory.")
    else:
        log_message(f"Deployment of {APP_NAME} failed.")

    log_message("--- Simulation End ---")

    # Optional: Clean up build artifacts after deployment
    # if os.path.exists(BUILD_ARTIFACT_DIR):
    #     shutil.rmtree(BUILD_ARTIFACT_DIR)
    #     log_message(f"Cleaned up build artifacts directory '{BUILD_ARTIFACT_DIR}'.")
