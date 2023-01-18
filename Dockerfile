FROM python

RUN apt-get update && apt-get install -y --no-install-recommends \
    bzip2 \
    g++ \
    git \
    graphviz \
    libgl1-mesa-glx \
    libhdf5-dev \
    openmpi-bin \
    wget \
    libopencv-dev \
    python3-opencv \
    python3-tk && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

RUN usermod -a -G video root
RUN usermod -a -G root root

EXPOSE 8123

ENTRYPOINT [ "python3" ]
CMD ["app.py"]