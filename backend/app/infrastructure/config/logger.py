import logging
import os
import sys
from pathlib import Path

import structlog

_IS_CONFIGURED = False


def setup_logger() -> None:
    # variable for indempotencie
    global _IS_CONFIGURED

    if _IS_CONFIGURED:
        return

    # Environment Variables
    log_level = os.getenv("PT_LOG_LEVEL", "INFO").upper()
    log_dir = os.getenv("PT_LOG_DIR", "logs")
    log_path = Path(log_dir) / "pt.log.jsonl"

    # Ensure directory exists
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # Shared Processors
    # These process the data BEFORE it is rendered into a string
    shared_processors = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
    ]

    # Define Handlers
    # Console Handler: Pretty Printing
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(
        structlog.stdlib.ProcessorFormatter(
            processor=structlog.dev.ConsoleRenderer(colors=True),
            foreign_pre_chain=shared_processors,
        )
    )

    # File Handler: JSON Printing
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(
        structlog.stdlib.ProcessorFormatter(
            processor=structlog.processors.JSONRenderer(),
            foreign_pre_chain=shared_processors,
        )
    )

    # Standard Logging Root Setup
    root_logger = logging.getLogger()

    # IMPORTANT: Clear existing handlers (like Uvicorn's defaults)
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
        try:
            handler.close()
        except Exception:
            pass

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
    root_logger.setLevel(log_level)

    # Force Uvicorn loggers to propagate to the root logger we just configured
    for name in ["uvicorn", "uvicorn.error", "uvicorn.access"]:
        logging_logger = logging.getLogger(name)
        logging_logger.handlers = []
        logging_logger.propagate = True

    # Structlog Configuration
    structlog.configure(
        processors=[
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    # Use standard library sys.stderr to bypass potential print buffering
    sys.stderr.write(f"Logger configured. Level: {log_level} | File: {log_path}\n")
    sys.stderr.flush()

    _IS_CONFIGURED = True
