
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Retrain Model') {
            steps {
                sh '''
                    /home/preetshah0407/app/venv/bin/python retrain.py
                    test -s iris_model.pkl
                '''
            }
        }

        stage('Deploy Model') {
            steps {
                sh '''
                    sudo cp iris_model.pkl /home/preetshah0407/app/iris_model.pkl
                    sudo chown preetshah0407:preetshah0407 /home/preetshah0407/app/iris_model.pkl
                    test -s /home/preetshah0407/app/iris_model.pkl
                '''
            }
        }
    }

    post {
        success {
            echo 'Model retrained and deployed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check the Console Output.'
        }
    }
}
