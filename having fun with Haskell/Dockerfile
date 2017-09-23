FROM ubuntu

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y build-essential
RUN apt-get install -y gcc
RUN apt-get install -y libpq-dev
RUN apt-get install -y vim
RUN apt-get install -y curl
#RUN add-apt-repository ppa:hvr/ghc
#RUN apt-get update
#RUN apt-get install ghc-8.0.2

RUN curl -sSL https://get.haskellstack.org/ | sh
RUN mkdir -p my
RUN cd my/
RUN stack setup
#RUN stack build
#RUN stack ghci



ENTRYPOINT ["/bin/bash"]

run echo "DONE"
