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
    stage('Buld docker'){
        steps{
            sh 'docker compose up -d --no-color --wait'
            sh 'docker compose ps'
        }
    }
}
