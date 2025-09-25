"""
pytest 設定檔
"""
import pytest
import sys
from pathlib import Path

# 將 parent 目錄加入 Python path
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))


@pytest.fixture
def sample_array():
    """提供測試用的陣列"""
    return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


@pytest.fixture
def sorted_array():
    """提供已排序的陣列"""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@pytest.fixture
def empty_array():
    """提供空陣列"""
    return []


@pytest.fixture
def single_element_array():
    """提供單一元素陣列"""
    return [42]


@pytest.fixture
def duplicate_array():
    """提供含重複元素的陣列"""
    return [5, 2, 8, 2, 9, 1, 5, 5]