import importlib

import pytest

np = pytest.importorskip("numpy")

spec = importlib.util.spec_from_file_location(
    "metrics", "alphaevolve/evaluator/metrics.py"
)
metrics = importlib.util.module_from_spec(spec)
spec.loader.exec_module(metrics)


def test_sharpe_short_series_returns_zero():
    assert metrics.sharpe(np.array([0.01])) == 0.0
