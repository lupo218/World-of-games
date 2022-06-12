pipeline {
    agent any

    stages {
        stage('check docker') {
            steps {
                sh '''
                docker version
                docker info
                docker compose version 
                '''
            }
        }
    }
    stages{
        steps('Buld docker'){
            sh 'docker compose up -d --no-color --wait'
            sh 'docker compose ps'
        }
    }
}
