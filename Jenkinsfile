pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-u root'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                sh 'ls -la'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt pytest pytest-html webdriver-manager'
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
