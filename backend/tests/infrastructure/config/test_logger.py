import logging
from pathlib import Path

import pytest

import app.infrastructure.config.logger as logger_module


@pytest.fixture
def reset_root_logger_state():
    root_logger = logging.getLogger()

    old_handlers = root_logger.handlers[:]
    old_level = root_logger.level
    old_flag = logger_module._IS_CONFIGURED

    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
        try:
            handler.close()
        except Exception:
            pass

    logger_module._IS_CONFIGURED = False

    yield

    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
        try:
            handler.close()
        except Exception:
            pass

    for handler in old_handlers:
        root_logger.addHandler(handler)

    root_logger.setLevel(old_level)
    logger_module._IS_CONFIGURED = old_flag


def test_setup_logger_uses_env_values(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    reset_root_logger_state,
):
    monkeypatch.setenv("PT_LOG_LEVEL", "DEBUG")
    monkeypatch.setenv("PT_LOG_DIR", str(tmp_path))

    logger_module.setup_logger()

    root_logger = logging.getLogger()

    assert root_logger.level == logging.DEBUG
    assert len(root_logger.handlers) == 2
    assert (tmp_path / "pt.log.jsonl").exists()


def test_setup_logger_is_idempotent(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    reset_root_logger_state,
):
    monkeypatch.setenv("PT_LOG_LEVEL", "INFO")
    monkeypatch.setenv("PT_LOG_DIR", str(tmp_path))

    logger_module.setup_logger()
    first_handlers = list(logging.getLogger().handlers)

    logger_module.setup_logger()
    second_handlers = list(logging.getLogger().handlers)

    assert len(first_handlers) == 2
    assert len(second_handlers) == 2
    assert first_handlers == second_handlers


def test_setup_logger_defaults_when_env_missing(
    monkeypatch: pytest.MonkeyPatch,
    reset_root_logger_state,
):
    monkeypatch.delenv("PT_LOG_LEVEL", raising=False)
    monkeypatch.delenv("PT_LOG_DIR", raising=False)

    logger_module.setup_logger()

    root_logger = logging.getLogger()

    assert root_logger.level == logging.INFO
    assert len(root_logger.handlers) == 2


def test_uvicorn_loggers_propagate_to_root(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    reset_root_logger_state,
):
    monkeypatch.setenv("PT_LOG_DIR", str(tmp_path))

    logger_module.setup_logger()

    for name in ["uvicorn", "uvicorn.error", "uvicorn.access"]:
        logger = logging.getLogger(name)
        assert logger.handlers == []
        assert logger.propagate is True
