pipeline {
    agent any

    environment {
        DJANGO_SETTINGS_MODULE = "bookstore.settings"
        PATH = "/opt/homebrew/bin:$PATH"
    }

    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'pwd'
                sh 'docker-compose build'
            }
        }

        stage('Run Tests') {
            steps {
                // If tests fail, this will stop the pipeline
                sh 'docker-compose run --rm web python manage.py test'
            }
        }

        stage('Deploy App') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        failure {
            echo '❌ Pipeline failed. Check test or deployment stage.'
        }
        success {
            echo '✅ Pipeline succeeded.'
        }
    }
}
