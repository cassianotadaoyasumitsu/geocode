# Base image
FROM python:3.12.0-slim-bookworm

# Create a non-root user
RUN groupadd -r nonroot && useradd -r -g nonroot nonroot

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get install -y build-essential \
    && apt-get clean autoclean \
    && apt-get autoremove -y --purge \
    && rm -rf \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/* \
    /usr/share/man \
    /usr/share/doc \
    /usr/share/doc-base

RUN mkdir -p /app
WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY ./ /app/

# Change ownership to non-root user
RUN chown -R nonroot:nonroot /app

# Switch to the non-root user
USER nonroot

ENTRYPOINT ["/usr/local/bin/flask"]
CMD ["run", "--host=0.0.0.0"]
