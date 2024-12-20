FROM python:3.14-rc-bullseye as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    POETRY_VERSION=1.8.4 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    TESSERACT_VERSION=5.5.0

RUN apt-get update && apt-get install -y \
    git \
    wget \
    g++ \
    make \
    autoconf \
    automake \
    libtool \
    pkg-config \
    libpng-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libleptonica-dev \
    libicu-dev \
    libpango1.0-dev \
    libcairo2-dev \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/tesseract-ocr/tesseract/archive/${TESSERACT_VERSION}.tar.gz \
    && tar -xzvf ${TESSERACT_VERSION}.tar.gz \
    && cd tesseract-${TESSERACT_VERSION} \
    && ./autogen.sh \
    && ./configure \
    && make \
    && make install \
    && ldconfig \
    && cd .. \
    && rm -rf tesseract-${TESSERACT_VERSION} ${TESSERACT_VERSION}.tar.gz

RUN pip install "poetry==$POETRY_VERSION"
WORKDIR /snapOCR
COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-dev

COPY . .

RUN poetry install --no-dev

CMD ["poetry", "run", "python", "main.py"]