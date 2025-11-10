#!/bin/bash

# Wait for database to be ready
echo "Waiting for database..."
while ! nc -z localhost 5432; do
  sleep 0.1
done
echo "Database started"

# Run migrations
echo "Running database migrations..."
alembic upgrade head

# Start the application
echo "Starting FastAPI server..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload