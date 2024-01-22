pipeline {
    agent {
        docker {
            image 'python:3.8' // Use the Python image to test your package
            args '-v /var/run/docker.sock:/var/run/docker.sock' // Mount Docker socket
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'echo "Building Image..."'
                // Add commands to build your Docker image here
                sh 'docker build -t your-image-name .'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Running Tests..."'
                // Run your test commands here
                sh 'python -m unittest'
            }
        }
    }
}
