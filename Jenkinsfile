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
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'anuka264/exam-app'
        IMAGE_TAG  = "build-${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Code already checked out automatically via Pipeline script from SCM.'
                sh 'ls -la'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Push to Registry') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }

        stage('Run Container') {
            steps {
                sh "docker run -d -p 3000:3000 --name exam-app-${BUILD_NUMBER} ${IMAGE_NAME}:${IMAGE_TAG}"
            }
        }
    }
}
