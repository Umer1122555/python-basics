pipeline {
    agent any
    
    stages {
        stage('Setup') {
            steps {
                echo 'Starting Capstone Pipeline...'
                bat 'py -m pip install -r requirements.txt'
            }
        }
        
        stage('Run Parallel Tests') {
            steps {
                // triple quotes se space wala path issue khatam ho jayega
                bat '''
                    py -m pytest -n 2 -v --html=report.html --self-contained-html
                '''
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
            
            echo "Build finished with status: ${currentBuild.currentResult}"
            
            emailext (
                to: 'umerkhan2211e@gmail.com',
                subject: "Capstone Build #${env.BUILD_NUMBER} - ${currentBuild.currentResult}",
                body: "Build ${currentBuild.currentResult}. Please check the attached report or Jenkins.",
                attachLog: true,
                attachmentsPattern: 'report.html'
            )
        }
    }
}