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
                git branch: 'main', url: 'https://github.com/Anuka264/webdriver-manager.git'
            }
        }

        stage('Build') {
            steps {
                sh '''
                    apt-get update && apt-get install -y wget gnupg unzip curl
                    curl -fsSL https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /etc/apt/trusted.gpg.d/google-archive-keyring.gpg
                    echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/google-archive-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list
                    apt-get update
                    apt-get install -y google-chrome-stable
                    pip install -r selenium-tests/requirements.txt pytest pytest-html
                '''
            }
        }

        stage('Test') {
            steps {
                dir('selenium-tests') {
                    sh 'pytest --junitxml=report.xml --html=report.html --self-contained-html -v'
                }
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'selenium-tests/report.xml'
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'selenium-tests',
                reportFiles: 'report.html',
                reportName: 'Selenium HTML Report',
                reportTitles: 'Selenium Test Report'
            ])
        }
    }
}
