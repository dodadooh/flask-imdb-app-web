
Flask IMDb App Web
This project provides a Flask web application that reads IMDb export CSV files and serves them as a JSON list through a web interface. The app is designed to be run inside a Docker container, making it easy to deploy and manage in various environments.

Features
Parses IMDb export CSV files.
Serves movie data through a /get-list endpoint in JSON format.
Easy to deploy via Docker.
Requirements
Docker installed on your system (Docker Desktop, Docker Engine, or Docker on a compatible server).

Project Structure

flask-imdb-app/
│
├── imdb_exports/        # Directory containing IMDb export CSV files
│   ├── movie1.csv
│   ├── movie2.csv
│   └── ...
│
├── app.py               # Flask application
├── Dockerfile           # Dockerfile for building the Docker image
├── requirements.txt     # Python dependencies
└── templates/           # Directory for HTML templates
    └── index.html       # Frontend HTML file

Setup Instructions
1. Build the Docker Image
To get started, you'll need to build the Docker image for the Flask IMDb app.

docker build -t flask-imdb-app-web .

2. Run the Docker Container
Once the image is built, you can run the Docker container. You'll need to map a directory from your host machine into the container where the IMDb export CSV files are stored.

docker run -d -p 5000:5000 -v /path/to/your/csvs:/app/imdb_exports flask-imdb-app-web
/path/to/your/csvs: Replace this with the actual path to the directory on your host machine where your IMDb export CSV files are stored.
/app/imdb_exports: This is the directory inside the container where the CSV files will be accessible.

3. Access the Application
After starting the container, the Flask application will be accessible via your web browser:

http://localhost:5000/get-list
If you're running the container on a remote server or in an environment like Unraid, replace localhost with the IP address of that server.

Troubleshooting
Common Issues
No CSV Files Found:

Ensure that the /path/to/your/csvs directory on your host is correctly mapped to /app/imdb_exports inside the container.

Verify that the CSV files are correctly placed in the directory you mapped.
Access Issues:

Check that the container is running and accessible on port 5000.
Ensure there are no firewall rules blocking access to the specified port.
Docker Logs:

To debug issues, view the container logs using:


docker logs <container_id>
Checking Container Status
You can check the status of the running container by using:

License
This project is licensed under the MIT License. See the LICENSE file for details.

