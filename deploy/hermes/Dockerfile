FROM nousresearch/hermes-agent:latest

USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends chromium curl \
    && rm -rf /var/lib/apt/lists/*

ENV AGENT_BROWSER_EXECUTABLE_PATH=/usr/bin/chromium \
    AGENT_BROWSER_ENGINE=chrome \
    AGENT_BROWSER_ARGS=--no-sandbox,--disable-dev-shm-usage

USER hermes
