pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat '"C:\\Windows\\System32\\cmd.exe" /c python --version'
      }
    }
    stage('STAGE2') {
      steps {
        bat '"C:\\Windows\\System32\\cmd.exe" /c python test1.py %X_VALUE% %Y_VALUE%'
      }
    }
  }
}
