## CoderCo Containers Challenge — Flask + Redis App

# Overview

This project is a multi-container Docker application built using Flask and Redis.

The Flask app provides two routes:
	•	/ → Welcome message
	•	/count → Increments and displays a visit counter stored in Redis

The application runs using Docker Compose, and Redis data is stored using a persistent volume.

⸻

# What I Built
	•	A Python Flask web application
	•	A Redis key-value database
	•	Two Dockerfiles (one for Flask, one for Redis)
	•	A Docker Compose setup that:
	•	Builds and runs both services
	•	Connects them using an internal Docker network
	•	Uses environment variables for configuration
	•	Uses a Redis volume for persistence

⸻

 # How It Works
	•	Flask connects to Redis using:

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)


	•	Redis stores the visit counter under the key "visit_count".
	•	The /count route automatically increments the value on each refresh.
	•	docker-compose.yml orchestrates the entire application:
	•	Builds both images
	•	Maps Flask to port 5001
	•	Creates a Redis volume for stored data

⸻

# What I Learned
	•	How multi-container applications communicate internally
	•	How to write Dockerfiles for separate services
	•	How to debug port conflicts and container exit codes
	•	How to use Docker volumes for persistent storage
	•	How environment variables make services configurable
	•	How Redis works as an in-memory data store

⸻

# Debugging Notes

**Key issues I solved:**
	•	_name_ typo causing Flask container to exit
	•	Port mismatch (5001:5000 vs Flask running on port 5001)
	•	Requirements not installed → imports not resolving
	•	Rebuilding containers properly with --build
	•	Ensuring Redis host and port match Compose config

These helped me fully understand how container networking and Flask-Redis communication work.

⸻

# Running the Project

docker compose up --build

Then visit:
	•	http://localhost:5001
	•	http://localhost:5001/