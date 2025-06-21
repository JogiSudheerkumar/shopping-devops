pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/JogiSudheerkumar/shopping-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t shopping-app .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop & remove old container if exists
                    sh '''
                        docker stop shopping_container || true
                        docker rm shopping_container || true
                        docker run -d -p 5000:5000 --name shopping_container shopping-app
                    '''
                }
            }
        }
    }
}
