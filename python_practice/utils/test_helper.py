"""
測試輔助工具
"""
import time
import tracemalloc
from functools import wraps
from typing import Callable, Any


def measure_performance(func: Callable) -> Callable:
    """
    裝飾器：測量函數執行時間和記憶體使用量
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        # 開始記憶體追蹤
        tracemalloc.start()
        start_time = time.perf_counter()

        # 執行函數
        result = func(*args, **kwargs)

        # 結束測量
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        execution_time = end_time - start_time
        memory_mb = peak / (1024 * 1024)

        print(f"\n效能測試結果 - {func.__name__}:")
        print(f"執行時間: {execution_time:.4f} 秒")
        print(f"記憶體使用: {memory_mb:.2f} MB")

        return result

    return wrapper


def compare_algorithms(algorithms: list, test_data: Any, test_name: str = ""):
    """
    比較多個演算法的效能

    Args:
        algorithms: 要比較的演算法函數列表
        test_data: 測試資料
        test_name: 測試名稱
    """
    print(f"\n=== 演算法效能比較 {test_name} ===")
    results = []

    for algo in algorithms:
        tracemalloc.start()
        start_time = time.perf_counter()

        try:
            result = algo(test_data.copy() if hasattr(test_data, 'copy') else test_data)

            end_time = time.perf_counter()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            execution_time = end_time - start_time
            memory_mb = peak / (1024 * 1024)

            results.append({
                'name': algo.__name__,
                'time': execution_time,
                'memory': memory_mb,
                'result': result
            })

            print(f"{algo.__name__:20s}: {execution_time:.4f}s, {memory_mb:.2f}MB")

        except Exception as e:
            print(f"{algo.__name__:20s}: ERROR - {str(e)}")
            tracemalloc.stop()

    return results


def generate_test_data(data_type: str, size: int = 1000):
    """
    生成測試資料

    Args:
        data_type: 資料類型 ('random', 'sorted', 'reverse', 'duplicate')
        size: 資料大小
    """
    import random

    if data_type == 'random':
        return [random.randint(1, size) for _ in range(size)]
    elif data_type == 'sorted':
        return list(range(1, size + 1))
    elif data_type == 'reverse':
        return list(range(size, 0, -1))
    elif data_type == 'duplicate':
        return [random.randint(1, 10) for _ in range(size)]
    else:
        raise ValueError(f"不支援的資料類型: {data_type}")