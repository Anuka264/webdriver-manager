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
                sh 'pip install -r selenium-tests/requirements.txt pytest pytest-html'
            }
        }

        stage('Test') {
            steps {
                dir('selenium-tests') {
                    sh 'pytest test_suite.py --junitxml=report.xml --html=report.html --self-contained-html -v'
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
            junit 'selenium-tests/report.xml'                     
            publishHTML(target: [
                reportDir: 'selenium-tests',
                reportFiles: 'report.html',
                reportName: 'Selenium HTML Report',
                keepAll: true,
                alwaysLinkToLastBuild: true
            ])
        }
        failure {
            echo 'Build FAILED — one or more Selenium tests did not pass.'
        }
    }
}
