"""Tests for EnbPIForecaster."""

import sys
import types

from sktime.forecasting.enbpi import EnbPIForecaster


def test_get_test_params_handles_tsbootstrap_without_blockbootstrap(monkeypatch):
    """Ensure get_test_params does not fail on newer tsbootstrap API."""
    dummy_tsbootstrap = types.ModuleType("tsbootstrap")

    monkeypatch.setattr(
        "sktime.forecasting.enbpi._check_soft_dependencies",
        lambda *args, **kwargs: True,
    )
    monkeypatch.setitem(sys.modules, "tsbootstrap", dummy_tsbootstrap)

    params = EnbPIForecaster.get_test_params()

    assert isinstance(params, list)
    assert len(params) == 1
