pipeline {
    agent any

    environment {
        PYTHON_ENV = 'python3'
        TEST_FILE = 'tests.py'
    }

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up the environment...'
                // Create virtual environment and install dependencies
                sh '''
                ${PYTHON_ENV} -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Unit Test') {
            steps {
                echo 'Running unit test for YOLO model...'
                sh """
                source venv/bin/activate
                ${PYTHON_ENV} -m unittest ${TEST_FILE}
                """
            }
        }
    }

    post {
        always {
            echo 'Cleaning up environment...'
            sh 'rm -rf venv'
        }
        success {
            echo 'Unit test passed successfully!'
        }
        failure {
            echo 'Unit test failed. Please check the logs for details.'
        }
    }
}
