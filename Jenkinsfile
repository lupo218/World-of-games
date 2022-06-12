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
}