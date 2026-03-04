"""Tests for task-schedule."""

import pytest
from task_schedule import schedule


class TestSchedule:
    """Test suite for schedule."""

    def test_basic(self):
        """Test basic usage."""
        result = schedule("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            schedule("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = schedule(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
