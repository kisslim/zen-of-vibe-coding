FROM archlinux:latest

# Tenet 29: Restrict your AI in a terminal
# Tenet 30: But your terminal should be everywhere

# Install system dependencies
RUN pacman -Syu --noconfirm \
    python \
    python-pip \
    git \
    base-devel \
    sudo \
    expect \
    ollama

# Set up working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user for security
RUN useradd -m -s /bin/bash vibe-coder
RUN echo "vibe-coder ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Switch to non-root user
USER vibe-coder

# Set up Ollama (Tenet 13: Be the provider)
RUN ollama serve &
RUN sleep 10 && ollama pull deepseek-r1:8b

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "from vibe_coder.core import VirtualVibeCoder; print('Vibe Coder healthy')"

EXPOSE 8000

CMD ["python", "main.py"]