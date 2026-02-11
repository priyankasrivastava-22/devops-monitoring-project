pipeline {
    agent any

    environment {
        VENV = "venv"
        PYTHON = "python3"
    }

    options {
        timestamps()
    }

    stages {

        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                ${PYTHON} -m venv ${VENV}
                . ${VENV}/bin/activate
                pip install --upgrade pip
                pip install psutil
                '''
            }
        }

        stage('Run Monitoring Script') {
            steps {
                sh '''
                . ${VENV}/bin/activate
                ${PYTHON} scripts/monitor.py > monitoring_output.txt
                '''
            }
        }

        stage('Archive Logs') {
            steps {
                archiveArtifacts artifacts: 'monitoring_output.txt', fingerprint: true
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed. Please check logs."
        }
        always {
            echo "Build completed."
        }
    }
}
