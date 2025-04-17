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
        bat '"C:\\Windows\\System32\\cmd.exe" /c python parameter.py %X_VALUE% %Y_VALUE%'
      }
    }
  }
}
