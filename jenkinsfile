pipeline{
    agent any
    stages{
        stage ('Start'){
            steps{
                echo 'Pipeline started by Elvin'
            }
        }
        stage ('Checkout'){
            steps{
                git branch: 'main',
                    url: 'https://github.com/Xlvin95/Just_The-demo_app-Jenkins_Practice-.git'
            }
        }
        stage ('Build'){
            steps{
                echo 'Building The Application'
            }
        }
        stage ('Test'){
            steps{
                echo 'Testing the Application'
            }
        }
        stage ('Deploy'){
            steps{
                echo 'Deploying the Application'
            }
        }
      
    }
    post{
        success🚀{
            echo 'The pipleine the successful'
        }
        failure❌{
            echo 'The pipeline failed'
        }
    }
}    
