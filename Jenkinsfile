pipeline {
    agent any

    stages {
        stage('check docker') {
            steps {
                sh '''
                docker version
                docker info
                docker compose version
                pip install -r requirements2.txt 
                '''
            }
        }
        stage('cleen old') {
            steps {
                sh '''
                    docker rm -f  $(docker ps |grep docker_from_git_wog |awk '{print $1}')
                    docker rmi -f  $(docker images |grep docker_from_git_wog |awk '{print $1}')
                '''
            }
        }
        stage('Buld docker'){
            steps {
                sh 'docker compose up -d --no-color --wait'
                sh 'docker compose ps'

            }
        }
        stage('Test URL'){
            steps {
                sh '''
                    var1 = $(/usr/bin/python3 e2e.py)
                    echo $var1

                  '''

            }
        }
    }
}
