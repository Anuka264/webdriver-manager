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
                    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
                    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
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

        stage('Archive') {
            when {
                expression { currentBuild.currentResult == 'SUCCESS' }
            }
            steps {
                archiveArtifacts artifacts: 'selenium-tests/*.png', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'selenium-tests/report.xml'
            archiveArtifacts artifacts: 'selenium-tests/report.html', allowEmptyArchive: true
        }
        failure {
            echo 'Build FAILED — one or more Selenium tests did not pass.'
        }
    }
}
