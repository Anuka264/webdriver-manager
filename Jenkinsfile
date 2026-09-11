pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-u root'
        }
    }
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'localhost:5000/exam-app'
        IMAGE_TAG  = "build-${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }

        stage('Push to Registry') {
            steps {
                sh 'docker push ${IMAGE_NAME}:${IMAGE_TAG}'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 3003:3003 --name exam-app-${BUILD_NUMBER} ${IMAGE_NAME}:${IMAGE_TAG}'
            }
        }
    }
}
