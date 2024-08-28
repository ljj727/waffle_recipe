pipeline {
    agent any

    environment {
        imagename = "fastapi-torch"
        // registryCredential = 'joon09'
        version = '0.1'
        dockerImage = ''
    }

    stages {

        // docker build
        stage('Bulid Docker') {
          agent any
          steps {
            echo 'Bulid Docker'
            echo "Building Docker image with name: ${imagename} and version: ${version}"  
            sh 'docker-compose build'
            // script {
            //     dockerImage = docker.build("${imagename}:${version}", "--no-cache .")
            // }
          }
          post {
            failure {
              error 'This pipeline stops here...'
            }
          }
        }

        // docker Deploy
        stage('Deploy Docker') {
          agent any
          steps {
            echo 'Deploy Docker '
            sh 'docker-compose up -d'
          }
          post {
            failure {
              error 'This pipeline stops here...'
            }
          }
        }

        // // docker push
        // stage('Push Docker') {
        //   agent any
        //   steps {
        //     echo 'Push Docker'
        //     script {
        //         docker.withRegistry( '', registryCredential) {
        //             dockerImage.push(version)  // ex) "1.0"
        //         }
        //     }
        //   }
        //   post {
        //     failure {
        //       error 'This pipeline stops here...'
        //     }
        //   }
        // }


    }
}