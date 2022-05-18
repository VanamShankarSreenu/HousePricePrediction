FROM continuumio/miniconda3

LABEL maintainer="Shankar Sreenu"

COPY /conda/linux_cpu_py39.yml env.yml

RUN conda env create -n housing -f env.yml

RUN git clone https://github.com/VanamShankarSreenu/HousePricePrediction

RUN cd  HousePricePrediction\
    &&   conda run -n housing \
    && pip install . \
    && pytest

CMD ["/bin/bash"]