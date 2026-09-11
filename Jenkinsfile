pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run Selenium Tests') {
            steps {
                withDockerContainer(image: 'python:3.11-slim', args: '-u root') {
                    sh '''
                        apt-get update && apt-get install -y \
                            wget curl unzip gnupg \
                            libxi6 libnss3 libatk-bridge2.0-0 libcups2 libdrm2 \
                            libxcomposite1 libxdamage1 libxrandr2 libgbm1 libasound2t64 \
                            libpango-1.0-0 libcairo2

                        wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg
                        echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list
                        apt-get update && apt-get install -y google-chrome-stable

                        pip install --no-cache-dir -r requirements.txt

                        pytest selenium-tests/ --junitxml=report.xml --html=report.html --self-contained-html -v
                    '''
                }
            }
        }
    }
    post {
        always {
            junit 'report.xml'
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: false,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Selenium HTML Report',
                reportTitles: 'Test Report'
            ])
        }
    }
}
