pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/sheraztariq22/ml-ci-cd-pipeline.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t sheraztariq22/ml-app:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub', url: '']) {
                    sh 'docker push sheraztariq22/ml-app:latest'
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh 'docker run -d -p 5000:5000 sheraztariq22/ml-app'
            }
        }

        stage('Notify Admin') {
            steps {
                emailext(
                    subject: "Deployment Successful",
                    body: "The ML application has been successfully deployed!",
                    to: "sheraztariq790@gmail.com"
                )
            }
        }

    }
}
