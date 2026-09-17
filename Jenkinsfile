pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t poc7-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker rm -f poc7-app || true
                docker run -d -p 5000:5000 --name poc7-app poc7-app
                '''
            }
        }
    }
}
