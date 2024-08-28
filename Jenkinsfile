pipeline {
    agent any
    environment {
        version = '0.1'
    }
    stages {
        stage('Bulid Docker') {
          agent any
          steps {
            echo 'Bulid Docker'
            sh 'tag=${version} docker compose build'
          }
          post {
            failure {
              error 'This pipeline stops here...'
            }
          }
        }
        stage('Stop and Remove Existing Containers') {  
          agent any
          steps {
            echo 'Container Stop Docker '
            sh 'tag=${version} docker compose down'
          }
        }  
        stage('Deploy Docker') {
          agent any
          steps {
            echo 'Deploy Docker '
            sh 'tag=${version} docker compose up -d'
          }
          post {
            failure {
              error 'This pipeline stops here...'
            }
          }
        }
    }
}