FROM ubuntu:latest
LABEL authors="dungca"

ENTRYPOINT ["top", "-b"]