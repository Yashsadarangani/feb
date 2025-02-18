pipeline{
    agent any
    environment{
        PYTHON_PATH = 'C:\\Users\\Yashu Kun\\AppData\\Local\\Programs\\Python\\Python312;C:\\Users\\Yashu Kun\\AppData\\Local\\Programs\\Python\\Python312\\Scripts'
        PATH = "${PATH};C:\\Windows\\System32"
    }
    stages{
        stage('Source Code'){
            steps{
                checkout scm
            }
        }
        stage('Build'){
            steps{
                bat'''
                echo "Building"
                set PATH=%PYTHON_PATH%;%PATH%
                pip install -r requirements.txt
                pip install coverage
                coverage run -m unittest discover
                coverage xml -o coverage.xml
                '''
            }
        }
        stage('Deploying the results in sonarqube'){
            steps{
                bat '''
                set PATH=%PYTHON_PATH%;%PATH%
                sonar-scanner.bat ^
                -Dsonar.projectKey=feb ^
                -Dsonar.sources=. ^
                -Dsonar.host.url=http://localhost:9000 ^
                -Dsonar.python.coverage.reportPaths=coverage.xml ^
                -Dsonar.token=sqp_c1fb379d14655c1c1c24cba97d75cbd14b4b12b1
                '''
            }
        }
    }
    post{
        success {
            echo "Pipeline executed successfully."
        }
        failure {
            echo "Pipeline failed. Please check the logs."
        }
    }
}
