inst_str = 'RUN apt install maven -y '

with open("Dockerfile", "a") as dockerfile:
    dockerfile.write(inst_str + "\n")
