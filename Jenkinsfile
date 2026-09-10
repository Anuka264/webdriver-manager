pipeline {
    agent {
        docker {
            image 'cypress/included:13.6.6'
            args '-u root --entrypoint=""'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Code already checked out automatically via Pipeline script from SCM.'
                sh 'ls -la'
            }
        }

        stage('Build') {
            steps {
                dir('cypress-tests') {
                    sh 'npm install'
                    sh 'npx cypress install'
                }
            }
        }

        stage('Test') {
            steps {
                dir('cypress-tests') {
                    sh 'npx cypress run --spec cypress/e2e/login.cy.js'
                }
            }
        }

        stage('Archive') {
            when {
                expression { currentBuild.currentResult == 'SUCCESS' }
            }
            steps {
                echo 'Archiving artifacts since Test stage passed...'
                archiveArtifacts artifacts: 'cypress-tests/cypress/**/*', allowEmptyArchive: true
            }
        }
    }
}
