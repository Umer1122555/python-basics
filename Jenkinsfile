pipeline {
    agent any
    
    stages {
        stage('Setup') {
            steps {
                echo 'Starting Capstone Pipeline...'
                bat '"C:\\Users\\New Computer Arena\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt'
            }
        }
        
        stage('Run Parallel Tests') {
            steps {
                bat '"C:\\Users\\New Computer Arena\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pytest -n 2 -v --html=report.html --self-contained-html'
            }
        }
    }
    
    post {
        always {
            publishHTML([
                allowMissing: false, 
                alwaysLinkToLastBuild: true, 
                keepAll: true, 
                reportDir: '.', 
                reportFiles: 'report.html', 
                reportName: 'Capstone Test Report'
            ])
            
            emailext (
                to: 'umerkhan2211e@gmail.com',
                subject: "Build ${env.BUILD_NUMBER} - ${currentBuild.currentResult}",
                body: "Build ${currentBuild.currentResult}",
                attachLog: true,
                attachmentsPattern: 'report.html'
            )
        }
    }
}