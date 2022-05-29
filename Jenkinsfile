properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/EllaGrd/DevOps2.git"
    }
    stage("show files"){
        bat "dir"
    }
}
