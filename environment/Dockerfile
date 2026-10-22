# AGENT container image. Bake the environment the agent works in. Do NOT copy solution/ or tests/.
FROM python:3.13-slim-bookworm@sha256:ed86c82274b3c69b52fb5820f358f0bd7df0b603332063cb5c6e32bd220c3e6e

WORKDIR /app
COPY /app

# Install standard core system libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install spreadsheet engines and dependencies with strict production-pinned version constraints
RUN pip install --no-cache-dir \
    openpyxl==3.1.5 \
    pandas==2.2.3 \
    yfinance==0.2.52

# Allocating parent path structures without baking or copying raw asset files
RUN mkdir -p /app/solution /app/solution/outputfile
