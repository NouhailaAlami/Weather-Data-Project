This simple weather pipeline demonstrates a **production-like ETL pipeline** built from scratch to strengthen data engineering fundamentals. The goal is to showcase:

- **Data Pipeline Development** - Building scalable, modular ETL workflows
- **Orchestration** - Using Apache Airflow to schedule and manage data tasks
- **Containerization** - Deploying services with Docker for reproducibility
- **Database Management** - Designing schemas and persisting data in PostgreSQL
- **Infrastructure as Code** - Managing entire stacks with docker-compose
- **Best Practices** - Error handling, logging, and clean code structure

## Tech Stack

- **Orchestration:** Apache Airflow 3.3.2rc1
- **Database:** PostgreSQL 15.19
- **Language:** Python 3.11
- **Containerization:** Docker & Docker Compose

## Prerequisites

- Docker & Docker Compose installed
- Python 3.11+
- PostgreSQL client (psql)

- ## Installation & Setup

# 1. Clone the repository
git clone https://github.com/NouhailaAlami/Weather-Data-Project.git
cd Weather-Data-Project

# 2. Start Docker containers
docker-compose up

# 3. Wait for Airflow to initialize 
You'll see: "Airflow is ready"

# 4. Access Airflow UI
Open browser: http://localhost:8000
Login with default credentials (see logs for password)

## Pipeline Workflow

The DAG (`orchestrator.py`) executes the following steps:

1. **Fetch Data** - Mock weather API call with location & temperature data
2. **Create Schema** - Initialize `dev.weather_data` table if it doesn't exist
3. **Insert Records** - Transform and store weather data into PostgreSQL
4. **Schedule** - Runs every 1 minute (configurable via `schedule=timedelta()`)

### Test Execution & Results

The DAG was executed successfully. The logs show the complete ETL workflow:
<img width="637" height="489" alt="image" src="https://github.com/user-attachments/assets/18f38f56-0ebf-481c-864e-1a33d32529df" />

