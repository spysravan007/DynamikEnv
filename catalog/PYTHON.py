PYTHON_V = input('Select Python version (2.7, 3.5, 3.6, 3.7, 3.8, 3.9) \nEnter input (2.7): ') or ''

if PYTHON_V == '2.7':
    PYTHON_V = ''

inst_str = "RUN apt install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt install -y python{PYTHON_V}".format(PYTHON_V = PYTHON_V)

with open("Dockerfile", "a") as dockerfile:
    dockerfile.write(inst_str + "\n")
