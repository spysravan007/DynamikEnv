JAVA_V = int(input('Select Java version \n1. java-8\n2. java-11\nEnter input (1): ') or 1)

inst_str = ''

if JAVA_V == 1:
    inst_str = 'RUN apt install openjdk-8-jdk -y'
elif JAVA_V == 2:
    inst_str = 'RUN apt install openjdk-11-jdk -y'

with open("Dockerfile", "a") as dockerfile:
    dockerfile.write(inst_str + "\n")
