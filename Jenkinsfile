pipeline {
    agent any
    environment {
        PYTHON_ENV = 'venv' // Virtual environment for Python dependencies
    }
    stages {
        stage('Setup Environment') {
            steps {
                script {
                    echo "Setting up Python environment"
                    // Create and activate a Python virtual environment
                    sh 'python3 -m venv ${PYTHON_ENV}'
                    sh '. ${PYTHON_ENV}/bin/activate && pip install --upgrade pip'
                    sh '. ${PYTHON_ENV}/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Train Model') {
            steps {
                script {
                    echo "Training the YOLO model"
                    // Train the YOLO model
                    sh '. ${PYTHON_ENV}/bin/activate && python train_yolo.py'
                }
            }
        }
        stage('Validate Model') {
            steps {
                script {
                    echo "Validating the YOLO model"
                    // Validate the YOLO model
                    sh '. ${PYTHON_ENV}/bin/activate && python validate_yolo.py'
                }
            }
        }
        stage('Test Model') {
            steps {
                script {
                    echo "Testing the YOLO model"
                    // Test the YOLO model
                    sh '. ${PYTHON_ENV}/bin/activate && python test_yolo.py --test-data data/test'
                }
            }
        }
        stage('Archive Results') {
            steps {
                script {
                    echo "Archiving results"
                    // Archive output files like metrics, logs, and model weights
                    archiveArtifacts artifacts: 'output/**/*', fingerprint: true
                }
            }
        }
    }
    post {
        always {
            echo "Cleaning up workspace"
            // Cleanup to avoid conflicts between builds
            cleanWs()
        }
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check the logs for details."
        }
    }
}
