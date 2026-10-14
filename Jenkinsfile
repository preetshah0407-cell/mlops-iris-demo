pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    set -e
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Retrain Model') {
            steps {
                sh '''
                    set -e
                    .venv/bin/python retrain.py
                    test -s iris_model.pkl
                    echo "Model training successful."
                '''
            }
        }

        stage('Deploy Model') {
            steps {
                sh '''
                    set -e
                    sudo install -o preetshah0407 -g preetshah0407 \
                        -m 644 iris_model.pkl \
                        /home/preetshah0407/app/iris_model.pkl
                    test -s /home/preetshah0407/app/iris_model.pkl
                    echo "Model deployment successful."
                '''
            }
        }
    }

    post {
        success {
            echo 'Model retrained and deployed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
