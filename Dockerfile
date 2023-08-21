FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit-pypi==2022.3.1b1
RUN pip install fcd
RUN pip install pandas

WORKDIR /repo
COPY . /repo
