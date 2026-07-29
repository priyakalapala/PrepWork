pipeline {
    agent any

    environment {
        APP_NAME = "Inventory"
        ENV = "QA"
    }
    stages {
        stage('Deploy') {
            steps {
                script {
                    echo "Application: ${env.APP_NAME}"
                    echo "Environment: ${env.ENV}"

                    if(env.ENV == "QA"){
                        echo "deploying to QA"
                        }
                    else{
                        echo "deploying to production"
                    }
                    def servers = ["Server1", "Server2", "Server3"]
                     for (server in servers) {
                        echo "Deploying to ${server}"
                    }
                    Switch(env.Env) {
                        case "DEV":
                         echo "Debug Mode"
                         break

                         case "QA":
                         echo "Testing Mode"
                         break

                         case "PROD":
                            echo "Production Mode"
                            break

                        default:
                            echo "Unknown Environment"
                    }

                }
            }
        }
    }
}