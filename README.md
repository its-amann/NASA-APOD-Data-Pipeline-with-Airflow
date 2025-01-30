# 🚀 NASA APOD Data Pipeline

<div align="center">
  <img src="_asserts/architecture of the Data Pipeline.png" alt="Architecture Diagram" width="800"/>
  
  *Architecture of the NASA APOD Data Pipeline*
</div>

## 📋 Table of Contents
- [Overview](#-overview)
- [Project Structure](#-project-structure)
- [Architecture](#-architecture)
- [Features](#-features)
- [Local Development & Deployment](#-local-development--deployment)
- [Cloud Development & Deployment](#-cloud-development--deployment)
- [Setup Instructions](#-setup-instructions)
- [Pipeline Details](#-pipeline-details)
- [Monitoring & Results](#-monitoring--results)
- [Tech Stack](#-tech-stack)
- [Project Files & Folders](#-project-files--folders)

## 🎯 Overview

This project implements a robust data pipeline that fetches daily astronomical images and data from NASA's APOD (Astronomy Picture of the Day) API. The pipeline performs ETL operations and stores the processed data in a PostgreSQL database. The project is implemented in two distinct deployment modes:

1. **Local Development & Deployment**: Using Docker containers for both Airflow and PostgreSQL
2. **Cloud Development & Deployment**: Using Astronomer Cloud for Airflow and AWS RDS for PostgreSQL

## 🔄 Project Structure

The project is organized into two main deployment paths:

### Local Development
- Docker-based deployment
- PostgreSQL running locally in Docker container
- Airflow running in separate Docker container
- Inter-container communication via Docker Compose
- Local database monitoring via DBeaver

### Cloud Development
- Astronomer Cloud platform for Airflow deployment
- AWS RDS for PostgreSQL database
- Remote database access configuration
- Cloud-based monitoring and management

## 🏗 Architecture

The data pipeline consists of three main components:
1. **Extract**: Fetches data from NASA's APOD API
2. **Transform**: Processes the API response
3. **Load**: Stores the data in PostgreSQL database (local/cloud)

<div align="center">
  <img src="_asserts/architecture of the Data Pipeline.png" alt="Architecture" width="800"/>
  
  *Overall System Architecture*
</div>

## ✨ Features

- **Automated Data Collection**: Daily fetches from NASA APOD API
- **Flexible Deployment**: Supports both local and cloud environments
- **Robust Data Storage**: PostgreSQL database integration
- **Monitoring & Logging**: Comprehensive execution tracking
- **Containerized**: Docker-based local deployment
- **Cloud-Ready**: Astronomer deployment support

## 💻 Local Development & Deployment

The local setup utilizes Docker containers for both Airflow and PostgreSQL:

### Docker Configuration
<div align="center">
  <img src="_asserts/docker compose yaml file photo.png" alt="Docker Compose" width="700"/>
  
  *Docker Compose Configuration for Local Development*
</div>

### Local Environment Setup
<div align="center">
  <img src="_asserts/photo of the running container in the docker desktop app.png" alt="Docker Running" width="700"/>
  
  *Docker Containers Running Locally*
</div>

### Local Airflow Interface
<div align="center">
  <img src="_asserts/terminal log of airflow is started and we can see the url from where we can access the admin panel.png" alt="Airflow Start" width="700"/>
  
  *Local Airflow Startup Log*
</div>

<div align="center">
  <img src="_asserts/airflow login page.png" alt="Airflow Login" width="700"/>
  
  *Local Airflow Web Interface*
</div>

## ☁️ Cloud Development & Deployment

The cloud deployment leverages Astronomer Cloud and AWS RDS:

### Astronomer Deployment
<div align="center">
  <img src="_asserts/the image shows the logs that we see after running astro login command in cli , that tells us to open the browser.png" alt="Astro Login" width="700"/>
  
  *Astronomer CLI Login Process*
</div>

<div align="center">
  <img src="_asserts/this image shows the content we see in the command line after running astro deploy command after login in astro  , here we are selesting the 1 deployment type from the list it has provided.png" alt="Astro Deploy" width="700"/>
  
  *Selecting Deployment Type in Astronomer*
</div>

<div align="center">
  <img src="_asserts/here we can see the image deployed sucessfully in the astronormer cloud.png" alt="Deployment Success" width="700"/>
  
  *Successful Astronomer Cloud Deployment*
</div>

### AWS RDS Setup
<div align="center">
  <img src="_asserts/the image show we are creating the postgres database in the aws rds to save the results here after we run the pipeline in the astronormer cloud .png" alt="RDS Setup" width="700"/>
  
  *AWS RDS Database Creation*
</div>

<div align="center">
  <img src="_asserts/here we setting the configraation of postgress databse in the aws rds , making  it accessible via public ,enabling public access.png" alt="RDS Config" width="700"/>
  
  *RDS Configuration & Public Access Setup*
</div>

<div align="center">
  <img src="_asserts/adding the one more inbound rule so we are able to access it , in the vpc setting in database.png" alt="Security Rules" width="700"/>
  
  *AWS Security Group Configuration*
</div>

## 🛠 Setup Instructions

### 1. NASA API Configuration

1. Obtain API key from NASA
<div align="center">
  <img src="_asserts/site page from where we get the api key of nasa.png" alt="NASA API" width="700"/>
  
  *NASA API Key Generation*
</div>

2. Configure in Airflow connections
<div align="center">
  <img src="_asserts/photo of telling from where we can find the connections in the airflow ui , under the admin.png" alt="Airflow Connections" width="700"/>
  
  *Airflow Connections Location*
</div>

<div align="center">
  <img src="_asserts/adding the nasa api connection in the ariflow.png" alt="NASA Connection" width="700"/>
  
  *NASA API Connection Setup*
</div>

### 2. Database Connections

#### Local Database Access
<div align="center">
  <img src="_asserts/here we are login in the  dbeaver console to query the postgres runiing on the docker desktop.png" alt="Local DB Access" width="700"/>
  
  *Local PostgreSQL Database Access via DBeaver*
</div>

#### Cloud Database Access
<div align="center">
  <img src="_asserts/updated the engpoint in the host column in airflow connection in postgres,since this time postgress is not running locally its on the aws cloud.png" alt="DB Connection Update" width="700"/>
  
  *Cloud Database Connection Configuration*
</div>

## 📊 Pipeline Details

### API Integration
<div align="center">
  <img src="_asserts/photo of the result when we hit the get request to the api.png" alt="API Response" width="700"/>
  
  *NASA API Response Data*
</div>

<div align="center">
  <img src="_asserts/photo of the image that we got after hitting the api with get request , in this api we daily get one image , we got url from the api then using that url to see the image.png" alt="API Image" width="700"/>
  
  *APOD Image Retrieved from API*
</div>

### DAG Execution
<div align="center">
  <img src="_asserts/the graph of the airflow telling that all the tasks run , giving the green signal , no any run is failed.png" alt="DAG Graph" width="700"/>
  
  *Local DAG Execution Graph*
</div>

<div align="center">
  <img src="_asserts/here showing the graph of the dag in airflow ui that we have just run in the astronormer cloud platform.png" alt="Cloud DAG" width="700"/>
  
  *Cloud Platform DAG Execution*
</div>

## 📈 Monitoring & Results

### Local Deployment Results
<div align="center">
  <img src="_asserts/showing the data stored in the postgres database in the table form.png" alt="Local Results" width="700"/>
  
  *Data in Local PostgreSQL Database*
</div>

### Cloud Deployment Results
<div align="center">
  <img src="_asserts/querying the data in stored in aws rds postgress using the dbeaver sql script.png" alt="Cloud Query" width="700"/>
  
  *Querying Cloud Database via DBeaver*
</div>

<div align="center">
  <img src="_asserts/here in the last image we are showing  the data stored in the aws rds postgres , we can see the data in the table form.png" alt="Cloud Results" width="700"/>
  
  *Data Retrieved from AWS RDS PostgreSQL*
</div>

## 🔧 Tech Stack

- **Apache Airflow**: Workflow orchestration
- **Docker**: Containerization
- **PostgreSQL**: Data storage
- **Astronomer**: Cloud deployment
- **AWS RDS**: Cloud database
- **DBeaver**: Database management

## 📁 Project Files & Folders

### Root Directory Files
- **docker-compose.yaml**: Orchestrates multi-container Docker application
  ```yaml
  # Key components:
  - airflow-webserver
  - postgres
  # Defines networking & volume configurations
  ```
- **Dockerfile**: Customizes Airflow image with required dependencies
- **requirements.txt**: Lists Python dependencies for the project
- **packages.txt**: Defines system-level package requirements
- **.gitignore**: Specifies Git-ignored files
- **.dockerignore**: Lists files excluded from Docker context

### /dags Directory
Contains the core data pipeline implementation:
```
/dags
├── etlpipeline.py    # Main DAG implementation
└── .airflowignore    # Airflow file exclusion rules
```

The `etlpipeline.py` implements the ETL workflow:
```python
# Key components:
def create_table():
    # Creates PostgreSQL table schema
    # Handles both local and cloud database setup

def extract_apod():
    # Connects to NASA APOD API
    # Fetches daily astronomical picture and data

def transform_data():
    # Processes API response
    # Extracts relevant fields and formats data

def load_data_to_postgres():
    # Stores processed data in PostgreSQL
    # Handles both local and cloud database connections
```

### /tests Directory
Contains test suites for DAG validation:
```
/tests
└── /dags
    └── test_dag_example.py    # DAG unit tests
```

Testing coverage includes:
- DAG structure validation
- Task dependency checks
- Default argument verification
- Schedule interval testing

### /_asserts Directory
Project documentation assets:
- System architecture diagrams
- Setup and configuration screenshots
- Deployment process documentation
- Database schema and connection images
- Results and monitoring screenshots

### Database Schema
The PostgreSQL table structure used in both local and cloud deployments:
```sql
CREATE TABLE nasa_data (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),        # Title of the astronomical image
    explanation TEXT,          # Detailed description
    url TEXT,                 # URL to the image
    date DATE,               # Publication date
    media_type VARCHAR(255)  # Type of media (image/video)
);
```

### Configuration Details

#### Local Development
- Docker Compose manages:
  - Airflow webserver and scheduler
  - Local PostgreSQL instance
  - Network connectivity between services
  - Volume persistence for data

#### Cloud Deployment
- Astronomer CLI configuration for Airflow deployment
- AWS RDS PostgreSQL setup
  - Public access configuration
  - Security group rules
  - Connection endpoint management

### Implementation Notes
- The DAG runs daily to fetch new astronomical images
- Error handling for API and database operations
- Configurable parameters for both deployment modes
- Logging and monitoring integration
- Data persistence and backup considerations

<div align="center">
  Made with ❤️ by Aman Agnihotri
</div>
