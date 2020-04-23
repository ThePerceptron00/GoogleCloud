FROM rocker/r-ver:3.4.4

RUN mkdir /home/analysis

COPY helloworld.r /home/analysis/helloworld.r

CMD R -e "source('/home/analysis/helloworld.r')"