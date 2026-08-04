pipeline {
    agent any
    environment {
        APP_ENV = "Kartheek"
        AWS_REGION = "Us- east -1"
    }

    stages {
        stage("build") {
            steps {
                script {
                    echo "Building in $(APP_ENV) environment"
                    env.APP_ENV2 = "Priya2"
                    if(env.APP_ENV2 == "Priya") {
                    echo "Hello $(env.APP_ENV2)!"
                    }
                    esle {
                        echo "user not recognised"
                    }
                     for (int i = 1; i <= 4; i++) {
                         echo "i = ${i}"
                     }
                }
            }
        }
    }
}




pipeline {
    agent any

    environment {
        APP_ENV = "DEV"
    }

    stages {
        stage ('Environment Check') {
            steps {
                script {
                     if (env.APP_ENV == "DEV") {
                        echo "Deploying to Development"
                    } else {
                        echo "Deploying to Production"
                    }
                }
            }
        }

    }
}


pipeline {
    agent any
    stages {
        stage("Loop Example") {
            steps {
                script {
                    for (int i =1; i<=5; i++) {
                                echo "i = ${i}"
                    }
                }
            }
        }
    }
}


pipeline {
    agent any

    stages {
        stage('Servers') {
            steps {
                script {

                    def servers = ["Dev", "QA", "UAT", "Prod"]

                    for (server in servers) {
                        echo "Deploying to ${server}"
                    }

                }
            }
        }
    }
}


pipeline {
    agent any
     stages {
        stage('Applications') {
            steps {
            script {
                 def apps = ["Billing", "Payment", "Orders"]
                 apps.each{
                    echo "Building ${it}"
                 }
                 }
            }
        }
     }
}


pipeline {
    agent any

    stages {
        stage('While Loop') {
            steps {
                script {

                    int i = 1
                    while (i <= 4) {
                        echo "Count ${i}"
                        i++
                    }

                }
            }
        }
    }
}


pipeline {
    agent any
    stages {
        stage('Even count') {
        steps {
            script {
                def numbers = [10, 20, 30, 40 ,50]
                int count = 0
                for (num in numbers) {
                    if (num%2 == 0) {
                        count++
                    }

                }
                echo "Even count = ${count}"
            }
        }
            
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Odd count') {
            steps {
                script {
                    def numbers = [10, 15, 20, 25, 30]
                    int count = 0

                    for (num in numbers) {
                        if (num % 2 != 0) {
                            count++
                        }
                    }

                    echo "Odd count = ${count}"
                }
            }
        }
    }
}

pipeline {
    agent any
    stages {
        stage('positive count') {
            steps {
                script {
                    def num = [10, 12, 14, 18, 19]
                    int count = 0
                    for (num in numbers) {
                       if (num > 0) {
                            count++
                        }
                    }
                      echo "Positive count = ${count}"
                    }
                }
            }
        }
    }


pipeline {
    agent any

    stages {
        stage('Multiples of 5') {
            steps {
                script {
                    def numbers = [11, 15, 20, 33, 40, 51]

                    for (num in numbers) {
                        if (num % 5 == 0) {
                            echo "${num}"
                        }
                    }
                }
            }
        }
    }
}


