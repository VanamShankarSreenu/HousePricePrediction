FROM continuumio/miniconda3

LABEL maintainer="Shankar Sreenu"

COPY /conda/linux_cpu_py39.yml env.yml

RUN conda env create -n housing -f env.yml

RUN conda install pandas

RUN conda install pytest

RUN pip install sklearn

RUN git clone https://github.com/VanamShankarSreenu/Module_4_Coding_Best_Practices

RUN cd Module_4_Coding_Best_Practices \
    && conda run -n housing pip install . 

RUN python3 Module_4_Coding_Best_Practices/tests/unit_tests/test_data_ingestion.py

CMD ["/bin/bash"]