pipeline {
    agent any

    stages {
        stage('Clone repo') {
            steps {
                git 'https://github.com/SRCEM-AIML/C60_YashRahangdale_Final-Assignment.git'
            }
        }

        stage('Build Docker images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Run Migrations') {
            steps {
                sh 'docker-compose exec web python manage.py migrate'
            }
        }

        stage('Collect Static Files') {
            steps {
                sh 'docker-compose exec web python manage.py collectstatic --noinput'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker-compose exec web python manage.py test'
            }
        }
    }
}
