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
                script {
                    try {
                        sh 'exit 1'
                    }
                    catch (all) {
                        echo 'Something failed, I should sound the klaxons!'
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
