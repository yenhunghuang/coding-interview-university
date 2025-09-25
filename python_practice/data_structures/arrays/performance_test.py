"""
Dynamic Array 效能測試

測試各種操作的時間複雜度，驗證理論分析是否正確。
"""

import time
import random
import sys
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

# 加入上層目錄以便 import
parent_dir = Path(__file__).parent.parent.parent
sys.path.insert(0, str(parent_dir))

from data_structures.arrays import DynamicArray
from utils.test_helper import measure_performance, compare_algorithms, generate_test_data


def test_push_performance():
    """測試 push 操作的時間複雜度"""
    print("=== Push 操作效能測試 ===")

    sizes = [1000, 5000, 10000, 20000, 50000]
    times = []

    for size in sizes:
        arr = DynamicArray()

        start_time = time.perf_counter()
        for i in range(size):
            arr.push(i)
        end_time = time.perf_counter()

        avg_time = (end_time - start_time) / size
        times.append(avg_time)

        print(f"Size: {size:6d}, Total: {end_time - start_time:.4f}s, Avg: {avg_time:.8f}s per push")

    # 繪製圖表
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, 'bo-', label='實際測量')
    plt.xlabel('陣列大小')
    plt.ylabel('平均時間 (秒/操作)')
    plt.title('Push 操作時間複雜度 - 應該是 O(1) amortized')
    plt.legend()
    plt.grid(True)
    plt.show()


def test_insert_performance():
    """測試 insert 操作的時間複雜度"""
    print("\n=== Insert 操作效能測試 ===")

    sizes = [1000, 2000, 3000, 4000, 5000]
    times = []

    for size in sizes:
        arr = DynamicArray()
        # 先填入一些元素
        for i in range(size):
            arr.push(i)

        # 測試在中間位置插入的時間
        insert_pos = size // 2
        start_time = time.perf_counter()

        for i in range(100):  # 插入 100 次取平均
            arr.insert(insert_pos, 999)

        end_time = time.perf_counter()
        avg_time = (end_time - start_time) / 100
        times.append(avg_time)

        print(f"Size: {size:6d}, Avg insert time: {avg_time:.6f}s")

    # 繪製圖表
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, 'ro-', label='實際測量')

    # 顯示理論 O(n) 曲線
    normalized_times = np.array(times) / times[0]
    normalized_sizes = np.array(sizes) / sizes[0]
    plt.plot(sizes, times[0] * normalized_sizes, 'g--', label='理論 O(n)')

    plt.xlabel('陣列大小')
    plt.ylabel('平均時間 (秒/操作)')
    plt.title('Insert 操作時間複雜度 - 應該是 O(n)')
    plt.legend()
    plt.grid(True)
    plt.show()


def test_find_performance():
    """測試 find 操作的時間複雜度"""
    print("\n=== Find 操作效能測試 ===")

    sizes = [1000, 2000, 3000, 4000, 5000]
    times_worst = []
    times_avg = []

    for size in sizes:
        arr = DynamicArray()
        # 填入隨機數據
        for i in range(size):
            arr.push(random.randint(1, size * 2))

        # 最壞情況：尋找不存在的元素
        start_time = time.perf_counter()
        for _ in range(100):
            arr.find(-1)  # 不存在的元素
        end_time = time.perf_counter()
        times_worst.append((end_time - start_time) / 100)

        # 平均情況：尋找中間位置的元素
        target = arr.at(size // 2)
        start_time = time.perf_counter()
        for _ in range(100):
            arr.find(target)
        end_time = time.perf_counter()
        times_avg.append((end_time - start_time) / 100)

        print(f"Size: {size:6d}, Worst: {times_worst[-1]:.6f}s, Avg: {times_avg[-1]:.6f}s")

    # 繪製圖表
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_worst, 'ro-', label='最壞情況 (找不到)')
    plt.plot(sizes, times_avg, 'bo-', label='平均情況')

    # 顯示理論 O(n) 曲線
    normalized_worst = np.array(times_worst) / times_worst[0]
    normalized_sizes = np.array(sizes) / sizes[0]
    plt.plot(sizes, times_worst[0] * normalized_sizes, 'r--', label='理論 O(n)')

    plt.xlabel('陣列大小')
    plt.ylabel('平均時間 (秒/操作)')
    plt.title('Find 操作時間複雜度 - 應該是 O(n)')
    plt.legend()
    plt.grid(True)
    plt.show()


def test_capacity_expansion():
    """測試容量擴展的時機和效率"""
    print("\n=== 容量擴展測試 ===")

    arr = DynamicArray(4)  # 從小容量開始
    capacities = [arr.capacity()]
    sizes = [arr.size()]

    print(f"初始: size={arr.size()}, capacity={arr.capacity()}")

    # 新增元素並記錄容量變化
    for i in range(50):
        arr.push(i)
        if arr.capacity() != capacities[-1]:
            print(f"擴容! size={arr.size()}, capacity={arr.capacity()}")
        capacities.append(arr.capacity())
        sizes.append(arr.size())

    # 移除元素並記錄容量變化
    print("\n開始移除元素...")
    while arr.size() > 0:
        old_capacity = arr.capacity()
        arr.pop()
        if arr.capacity() != old_capacity:
            print(f"縮容! size={arr.size()}, capacity={arr.capacity()}")
        capacities.append(arr.capacity())
        sizes.append(arr.size())

    # 繪製容量變化圖
    plt.figure(figsize=(12, 6))
    x = range(len(sizes))
    plt.plot(x, sizes, 'b-', label='實際大小')
    plt.plot(x, capacities, 'r-', label='容量')
    plt.xlabel('操作次數')
    plt.ylabel('大小/容量')
    plt.title('動態陣列容量管理')
    plt.legend()
    plt.grid(True)
    plt.show()


def compare_with_python_list():
    """與 Python 內建 list 比較效能"""
    print("\n=== 與 Python List 效能比較 ===")

    def dynamic_array_push(data):
        arr = DynamicArray()
        for item in data:
            arr.push(item)
        return arr

    def python_list_append(data):
        lst = []
        for item in data:
            lst.append(item)
        return lst

    test_data = list(range(10000))

    algorithms = [dynamic_array_push, python_list_append]
    compare_algorithms(algorithms, test_data, "Push/Append 比較")


def run_all_performance_tests():
    """執行所有效能測試"""
    print("開始執行 Dynamic Array 效能測試...\n")

    try:
        test_push_performance()
        test_insert_performance()
        test_find_performance()
        test_capacity_expansion()
        compare_with_python_list()

        print("\n所有效能測試完成！")

    except ImportError as e:
        if "matplotlib" in str(e):
            print("注意：matplotlib 未安裝，無法顯示圖表")
            print("安裝方式: pip install matplotlib")
        else:
            raise


if __name__ == "__main__":
    run_all_performance_tests()