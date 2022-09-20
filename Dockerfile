FROM nvidia/cuda:11.0.3-base-ubuntu20.04
CMD nvidia-smi

# Fix Nvidia issue
RUN sh -c 'echo "APT { Get { AllowUnauthenticated \"1\"; }; };" > /etc/apt/apt.conf.d/99allow_unauth'

RUN apt -o Acquire::AllowInsecureRepositories=true -o Acquire::AllowDowngradeToInsecureRepositories=true update
RUN apt-get install -y curl wget

RUN apt-key del 7fa2af80
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-keyring_1.0-1_all.deb
RUN dpkg -i cuda-keyring_1.0-1_all.deb
RUN rm -f /etc/apt/sources.list.d/cuda.list /etc/apt/apt.conf.d/99allow_unauth cuda-keyring_1.0-1_all.deb

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC F60F4B3D7FA2AF80

RUN apt-get update && apt-get upgrade -y

#set up environment
RUN apt-get install --no-install-recommends --no-install-suggests -y curl
RUN apt-get install unzip
RUN apt-get -y install python3.9
RUN apt-get -y install python3-pip

# Install Rust to fix Pip install issue
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs -y | sh

WORKDIR /stable_diffusion_server

COPY . .

RUN pip3 install -r requirements.txt

# WORKDIR /latent_lab/frontend

# RUN npm install && npm run build

WORKDIR /stable_diffusion_server

EXPOSE 3000

CMD [ "python3", "-u", "-m", "app"]