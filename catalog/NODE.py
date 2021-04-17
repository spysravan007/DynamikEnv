NODE_V = input('Enter Node version (10.15.2): ') or '10.15.2'

inst_str = "RUN apt install curl && \
    curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash && \
    export NVM_DIR=\"$HOME/.nvm\" && [ -s \"$NVM_DIR/nvm.sh\" ] && \. \"$NVM_DIR/nvm.sh\" && \
    nvm install {NODE_V}".format(NODE_V = NODE_V)
   
with open("Dockerfile", "a") as dockerfile:
    dockerfile.write(inst_str + "\n")

