from airflow import DAG
from airflow.decorators import task
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.hooks.base import BaseHook
from airflow.utils.dates import days_ago
import json


# Define the DAG
with DAG(
    dag_id='nasa_pipeline',
    start_date=days_ago(1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    # Task: Create Table
    @task
    def create_table():
        # Initialize the connection to the database
        postgres_hook = PostgresHook(postgres_conn_id='my_postgres_connection')

        # SQL query to create the table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS nasa_data (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            explanation TEXT,
            url TEXT,
            date DATE,
            media_type VARCHAR(255)
        )
        """
        postgres_hook.run(create_table_query)

    # Extract data from the API
    conn = BaseHook.get_connection('nasa_api')

    extract_data = SimpleHttpOperator(
        task_id='extract_apod',
        http_conn_id='nasa_api',  # This is the connection ID in Airflow
        endpoint='planetary/apod',  # API endpoint   
        method='GET',
        data={"api_key": conn.extra_dejson.get('api_key')},  # API key from connection
        response_filter=lambda response: response.json(),  # Corrected JSON response filter
        log_response=True
    )

    # Task: Transform the data
    @task
    def transform_data(response):
        apod_data = {
            'title': response.get('title', ''),
            'explanation': response.get('explanation', ''),
            'url': response.get('url', ''),
            'date': response.get('date', ''),
            'media_type': response.get('media_type', '')
        }
        return apod_data

    # Task: Load data into PostgreSQL
    @task
    def load_data_to_postgres(apod_data):
        postgres_hook = PostgresHook(postgres_conn_id='my_postgres_connection')

        # Create SQL query
        insert_query = """
        INSERT INTO nasa_data (title, explanation, url, date, media_type)
        VALUES (%s, %s, %s, %s, %s);
        """

        postgres_hook.run(
            insert_query,
            parameters=(
                apod_data['title'],
                apod_data['explanation'],
                apod_data['url'],
                apod_data['date'],
                apod_data['media_type']
            )
        )

    # Define task dependencies
    create_table() >> extract_data
    api_response = extract_data.output
    transformed_data = transform_data(api_response)
    load_data_to_postgres(transformed_data)
