FROM mcr.microsoft.com/playwright/python:v1.38.0-jammy

RUN apt-get update \
    && apt-get install -y python3.11 python3-pip nano \
    && python3.11 -m pip install --no-cache-dir --upgrade pip \
    && python3.11 -m pip install --no-cache-dir playwright

WORKDIR /app

COPY pages /app/pages
COPY tests /app/tests
COPY components /app/components
COPY page_factory /app/page_factory
COPY conftest.py /app/
COPY config.py /app/
COPY requirements.txt /app/

RUN rm -rf /ms-playwright/* \
    && python3.11 -m playwright install chromium \
    && chmod -Rf 777 /ms-playwright \
    # && mv /ms-playwright/firefox-* /ms-playwright/firefox \
    # && mv /ms-playwright/webkit-* /ms-playwright/webkit \
    && pip install --no-cache-dir -r requirements.txt

