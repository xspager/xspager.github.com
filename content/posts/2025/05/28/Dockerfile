FROM ubuntu:24.04

ENV DEBIAN_FRONTEND="noninteractive"

# Development tools and other tools we will need
RUN apt-get update -y && apt-get install -y tzdata && apt-get install -y build-essential curl mtools unzip gnu-efi ovmf libedit2 && apt-get clean

#RUN groupadd -g 1000 user && useradd -u 1000 -m -g user user

RUN mkdir /hello
RUN chown ubuntu:ubuntu /hello

# As user ubuntu download, check the sha256 hash of the file, then extracts it
USER ubuntu
WORKDIR /hello
RUN curl -s -L -O https://github.com/terralang/terra/releases/download/release-1.2.0/terra-Linux-x86_64-cc543db.tar.xz
RUN echo "32f6420330de4d7176396aa36929a76733fe5a1fbc5a0cf8b9a6d270f9630d8d terra-Linux-x86_64-cc543db.tar.xz" | sha256sum -c  && tar xf terra-Linux-x86_64-cc543db.tar.xz

USER root
RUN mv terra-Linux-x86_64-cc543db /opt/terra-linux

# put the bin folder on the user PATH for the user
USER ubuntu
RUN rm -f terra-Linux-x86_64-cc543db.tar.xz
RUN echo "PATH=$PATH:/opt/terra-linux/bin" >> ~/.bashrc

ENTRYPOINT [ "/bin/bash" ]