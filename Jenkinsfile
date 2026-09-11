pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-u root'
        }
    }

    environment {
        NODE_TLS_REJECT_UNAUTHORIZED = '0'   // only if you hit the same TLS quirk as last night
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Code already checked out automatically via Pipeline script from SCM.'
                sh 'ls -la'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt pytest pytest-html'
            }
        }

        stage('Run Test Suite') {
            steps {
                sh 'pytest test_suite.py --junitxml=report.xml --html=report.html --self-contained-html -v'
            }
        }
    }

    post {
        always {
            junit 'report.xml'
            publishHTML(target: [
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Selenium HTML Report',
                keepAll: true,
                alwaysLinkToLastBuild: true
            ])
        }
    }
}
