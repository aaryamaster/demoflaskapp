pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'demo_flask_app'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/yourusername/DemoFlaskApp.git'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'
            }
            post {
                always {
                    junit 'tests/**/*.xml'
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build("${env.DOCKER_IMAGE}:${env.BUILD_ID}")
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    dockerImage.run('-p 5000:5000')
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}