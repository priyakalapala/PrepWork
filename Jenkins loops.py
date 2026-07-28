pipeline {
    agent any
    stages {
        stage('Nested Loop') {
            steps {
                script {

                    for (int i = 1; i <= 3; i++) {
                        for (int j = 1; j <= 2; j++) {
                            echo "i=${i}, j=${j}"

                        }

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
                    def numbers = [10, 15, 20, 25, 30]
                    int count = 0
                    for (num in numbers) {
                         if (num % 2 == 0) {
                            count++
                        }

                    }
                        echo "Even Count = ${count}"
                    
                }
            }
        }
    }
}


pipeline {
    agent any
    stages {
        stage('while loop') {
            steps {
                script {
                    int i=1
                    while (i<=3) {
                        echo "count ${i}"
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
        stage ("Map example") {
            steps {
                script {
                   def employee = [
                    Name : "priya"
                    Role : "DevOps"
                    City : "Phoenix"
                           ]
                employee.each {key, value -> echo "${key} : ${value}"
                }
                }
            }
        }
    }
}