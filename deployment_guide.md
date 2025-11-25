# Deployment Guide for AlbumELO

This guide explains how to deploy the AlbumELO application using Docker and Docker Compose. This setup is ideal for home servers like TrueNAS Scale.

## Prerequisites

- Docker and Docker Compose installed on your server.
- SSH access to your server (recommended).

## Project Structure

The deployment relies on the following files:
- `docker-compose.yml`: Orchestrates the Backend and Frontend services.
- `backend/Dockerfile`: Builds the Python FastAPI backend.
- `frontend/Dockerfile`: Builds the React frontend and serves it with Nginx.
- `frontend/nginx.conf`: Configures Nginx to serve the app and proxy API requests.

## Deployment Steps

### 1. Transfer Files
Copy the entire `AlbumELO` directory to your server. You can use `scp` or `git clone` if you push this to a repo.

```bash
scp -r AlbumELO user@your-server:/path/to/apps/
```

### 2. Run with Docker Compose
Navigate to the directory and start the services:

```bash
cd AlbumELO
docker-compose up -d --build
```

This command will:
- Build the backend and frontend images.
- Start the containers in detached mode.
- Create a `data` directory for persistent storage (SQLite database).

### 3. Access the Application
- **Frontend**: Open `http://<your-server-ip>` in your browser.
- **Backend API**: Accessible at `http://<your-server-ip>/api` (proxied by Nginx).

## TrueNAS Scale Specifics

If you are using TrueNAS Scale, you have a few options:

### Option A: "Custom App" (Docker Compose)
Recent versions of TrueNAS Scale support Docker Compose natively or via "Custom App".
1.  Create a new "Custom App".
2.  Paste the contents of `docker-compose.yml` into the configuration.
3.  **Important**: You may need to adjust the volume mappings. The default `./data:/app/data` assumes a relative path. In TrueNAS, you should map a Host Path to `/app/data` to ensure data persists across updates.

### Option B: Jail / VM
If you run a Linux VM or Jail, simply follow the standard Docker Compose steps above.

## Configuration

- **Database**: The SQLite database is stored in the `./data` directory. Back up this directory to save your data.
- **Ports**:
    - Frontend: Port `80` inside container, mapped to host port `80`.
    - Backend: Port `8000` inside container, mapped to host port `8000`.
    - To change the host port, edit `docker-compose.yml`:
      ```yaml
      ports:
        - "8080:80" # Maps host 8080 to container 80
      ```

## Troubleshooting

- **"Connection Refused"**: Ensure the containers are running with `docker-compose ps`.
- **Data not saving**: Check permissions on the `data` directory. Docker needs write access.
