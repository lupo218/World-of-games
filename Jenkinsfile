pipeline {
    agent any

    stages {
        stage('check docker & python') {
            steps {
                sh '''#!/bin/bash
                docker version
                docker info
                docker compose version
                pip install -r requirements2.txt 
                '''
            }
        }
        stage('cleen old docker') {
            steps {
                script {
                    try {
                        sh '''#!/bin/bash
                        docker rm -f  $(docker ps |grep docker_from_git_wog |awk '{print $1}')
                        docker rmi -f  $(docker images |grep docker_from_git_wog |awk '{print $1}')
                        '''
                    }
                    catch (all) {
                        echo 'No old docker to delete'
                    }
                }
        }   }
        stage('Buld docker'){
            steps {
                sh 'docker compose up -d --no-color --wait'
                sh 'docker compose ps'

            }
        }
        stage('Test URL'){
            steps {
                sh '''#!/bin/bash
                    var1=$(/usr/bin/python3 e2e.py 2>&1)
                    if [ var1='False' ]
                    then
                        echo 'Error on Url check !!!'
                        exit 1
                    else
                        echo 'Url check passed'
                        exit 0
                    fi
                  '''
            }
        }
    }
}
