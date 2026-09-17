pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t poc7-app .'
            }
        }

        stage('Deploy Using Ansible') {
            steps {
                sh 'ansible-playbook /home/ec2-user/ansible/deploy.yml'
            }
        }

    }
}
