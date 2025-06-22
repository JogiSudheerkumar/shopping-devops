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
                    bat 'docker build -t shopping-app .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    bat '''
                        docker stop shopping_container || exit 0
                        docker rm shopping_container || exit 0
                        docker run -d -p 5000:5000 --name shopping_container shopping-app
                    '''
                }
            }
        }
    }
}
