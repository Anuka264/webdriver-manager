pipeline {
    agent {
        docker {
            image 'cypress/included:13.6.6'
            args '-u root'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('cypress-tests') {
                    sh 'npm install'
                }
            }
        }

        stage('Run Cypress Test') {
            steps {
                dir('cypress-tests') {
                    sh 'npx cypress run --spec cypress/e2e/login.cy.js'
                }
            }
        }
    }

    post {
        success {
            echo 'Cypress test passed!'
        }
        failure {
            echo 'Cypress test failed — check console output above.'
        }
    }
}
