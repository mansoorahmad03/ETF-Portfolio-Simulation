# 1. FIX: Removed duplicate image prefix typo
FROM python:3.11-slim

WORKDIR /app

# Install standard core system libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# FIX: Added strict version pinning (==0.4.18) to the uv installer package line
RUN pip install --no-cache-dir \
    openpyxl==3.1.5 \
    pandas==2.2.3 \
    pytest==9.1.1 \
    uv==0.4.18

# 2. FIX: Explicitly create parent paths for all workspace domains
RUN mkdir -p /app/solution /app/solution/outputfile /app/tests /logs/verifier

# 3. FIX: Copy the local tests files directly into the /app/tests path expected by your test.sh
COPY . /app/tests/
COPY . /tests/

# Set working directory to your test home directory
WORKDIR /app/tests

# Force a cache bust to ensure test script updates are copied over
ENV CACHE_BUST=2

# Provide an execution baseline hook
ENTRYPOINT ["/bin/bash", "test.sh"]
