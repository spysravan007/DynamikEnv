FROM spysravan/codeserver 
RUN apt update
RUN apt install curl &&     curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash &&     export NVM_DIR="$HOME/.nvm" && [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" &&     nvm install 10.15.2 
RUN apt install openjdk-8-jdk -y 
RUN apt install maven -y 
RUN apt install software-properties-common -y &&     add-apt-repository ppa:deadsnakes/ppa -y &&     apt install python