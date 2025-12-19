#!/bin/sh

# Calcular número óptimo de workers
NUM_WORKERS=$(python -c "import multiprocessing; print(multiprocessing.cpu_count() * 2 + 1)")

echo "Iniciando Gunicorn con $NUM_WORKERS workers y 4 threads por worker"

exec gunicorn app:app \
    --workers $NUM_WORKERS \
    --threads 4 \
    --worker-class gthread \
    --timeout 120 \
    --bind 0.0.0.0:8000 \
    --access-logfile '-' \
    --error-logfile '-' \
    --log-level info
