pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            dir 'python_pipeline_jenkins_learn'
        }
    }
    stages {
        stage('Test') {
            steps {
                sh 'poetry run pytest'
            }
        }
    }
}