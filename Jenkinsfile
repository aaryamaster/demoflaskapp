pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/aaryamaster/demoflaskapp.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover -s tests'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying to production..."'
                // Add your deployment steps here
            }
        }
    }
}
