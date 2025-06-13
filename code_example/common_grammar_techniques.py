from typing import List, Dict, Tuple, Optional, Union, Any, Iterator, Generator
from collections import defaultdict, Counter
from itertools import zip_longest, chain
import operator


# ============= 1. enumerate() - 获取索引和值 =============
def demo_enumerate() -> None:
    """enumerate让你同时获取索引和元素值"""
    fruits: List[str] = ['apple', 'banana', 'cherry']

    # 基本用法
    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")

    # 自定义起始索引
    for index, fruit in enumerate(fruits, start=1):
        print(f"第{index}个: {fruit}")


# ============= 2. zip() - 并行迭代多个序列 =============
def demo_zip() -> None:
    """zip让你同时迭代多个序列"""
    names: List[str] = ['Alice', 'Bob', 'Charlie']
    ages: List[int] = [25, 30, 35]
    cities: List[str] = ['Beijing', 'Shanghai', 'Guangzhou']

    # 基本用法
    for name, age, city in zip(names, ages, cities):
        print(f"{name}, {age}岁, 来自{city}")

    # 创建字典
    person_dict: Dict[str, int] = dict(zip(names, ages))
    print(person_dict)

    # 解压缩（转置）
    pairs: List[Tuple[str, int]] = [('a', 1), ('b', 2), ('c', 3)]
    letters, numbers = zip(*pairs)
    print(letters, numbers)


# ============= 3. 列表推导式 - List Comprehensions =============
def demo_list_comprehensions() -> None:
    """列表推导式：简洁地创建列表"""
    numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 基本语法：[expression for item in iterable]
    squares: List[int] = [x ** 2 for x in numbers]

    # 带条件：[expression for item in iterable if condition]
    even_squares: List[int] = [x ** 2 for x in numbers if x % 2 == 0]

    # 嵌套循环
    matrix: List[List[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened: List[int] = [num for row in matrix for num in row]

    # 字符串处理
    words: List[str] = ['hello', 'world', 'python']
    capitalized: List[str] = [word.upper() for word in words if len(word) > 4]

    print(f"平方数: {squares}")
    print(f"偶数平方: {even_squares}")
    print(f"展平: {flattened}")
    print(f"大写: {capitalized}")


# ============= 4. 字典推导式和集合推导式 =============
def demo_dict_set_comprehensions() -> None:
    """字典和集合推导式"""
    words: List[str] = ['apple', 'banana', 'cherry', 'date']

    # 字典推导式：{key_expr: value_expr for item in iterable}
    word_lengths: Dict[str, int] = {word: len(word) for word in words}

    # 集合推导式：{expression for item in iterable}
    unique_lengths: set[int] = {len(word) for word in words}

    # 条件字典推导式
    long_words: Dict[str, int] = {word: len(word) for word in words if len(word) > 5}

    print(f"单词长度: {word_lengths}")
    print(f"唯一长度: {unique_lengths}")
    print(f"长单词: {long_words}")


# ============= 5. *args 和 **kwargs =============
def demo_args_kwargs(*args: Any, **kwargs: Any) -> None:
    """可变参数的使用"""
    print(f"位置参数: {args}")
    print(f"关键字参数: {kwargs}")


def flexible_function(required: str, *args: int, **kwargs: str) -> str:
    """灵活的参数处理"""
    result: str = f"必需参数: {required}"
    if args:
        result += f", 额外参数: {args}"
    if kwargs:
        result += f", 关键字参数: {kwargs}"
    return result


# ============= 6. 解包操作符 * 和 ** =============
def demo_unpacking() -> None:
    """解包操作符的强大用法"""
    # 列表解包
    numbers: list[int] = [1, 2, 3, 4, 5]
    first, *middle, last = numbers
    print(f"首: {first}, 中: {middle}, 尾: {last}")

    # 函数调用时解包
    def add_three(a: int, b: int, c: int) -> int:
        return a + b + c

    args: tuple[int, int, int] = (1, 2, 3)
    result: int = add_three(*args)
    print(f"result: {result}")

    # 字典解包
    dict1: dict[str, int] = {'a': 1, 'b': 2}
    dict2: dict[str, int] = {'c': 3, 'd': 4}
    merged: dict[str, int] = {**dict1, **dict2}
    print(f"合并字典: {merged}")


# ============= 7. 三元运算符 =============
def demo_ternary_operator() -> None:
    """三元运算符：简洁的条件表达式"""
    age: int = 20

    # 语法：value_if_true if condition else value_if_false
    status: str = "成年人" if age >= 18 else "未成年人"

    # 链式三元运算符
    score: int = 85
    grade: str = "优秀" if score >= 90 else "良好" if score >= 80 else "及格" if score >= 60 else "不及格"

    print(f"状态: {status}")
    print(f"等级: {grade}")


# ============= 8. Lambda函数 =============
def demo_lambda() -> None:
    """Lambda函数：简洁的匿名函数"""
    numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 基本lambda
    square = lambda x: x ** 2

    # 与内置函数结合使用
    even_numbers: List[int] = list(filter(lambda x: x % 2 == 0, numbers))
    squared_numbers: List[int] = list(map(lambda x: x ** 2, numbers))

    # 排序中使用lambda
    students: List[Tuple[str, int]] = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
    sorted_by_grade: List[Tuple[str, int]] = sorted(students, key=lambda x: x[1], reverse=True)

    print(f"偶数: {even_numbers}")
    print(f"平方: {squared_numbers}")
    print(f"按成绩排序: {sorted_by_grade}")


# ============= 9. map(), filter(), reduce() =============
def demo_functional_programming() -> None:
    """函数式编程工具"""
    from functools import reduce

    numbers: List[int] = [1, 2, 3, 4, 5]

    # map(): 对每个元素应用函数
    squared: List[int] = list(map(lambda x: x ** 2, numbers))

    # filter(): 过滤元素
    even: List[int] = list(filter(lambda x: x % 2 == 0, numbers))

    # reduce(): 累积操作
    sum_all: int = reduce(lambda x, y: x + y, numbers)
    product: int = reduce(lambda x, y: x * y, numbers)

    print(f"映射: {squared}")
    print(f"过滤: {even}")
    print(f"求和: {sum_all}")
    print(f"乘积: {product}")


# ============= 10. any() 和 all() =============
def demo_any_all() -> None:
    """any()和all()：布尔聚合函数"""
    numbers: List[int] = [2, 4, 6, 8]
    mixed: List[int] = [1, 2, 3, 4]

    # all(): 所有元素都为True
    all_even: bool = all(x % 2 == 0 for x in numbers)

    # any(): 至少一个元素为True
    has_even: bool = any(x % 2 == 0 for x in mixed)

    # 实际应用
    words: List[str] = ['hello', 'world', 'python']
    all_lowercase: bool = all(word.islower() for word in words)
    has_long_word: bool = any(len(word) > 5 for word in words)

    print(f"都是偶数: {all_even}")
    print(f"有偶数: {has_even}")
    print(f"都是小写: {all_lowercase}")
    print(f"有长单词: {has_long_word}")


# ============= 11. defaultdict 和 Counter =============
def demo_collections() -> None:
    """collections模块的强大工具"""

    # defaultdict: 自动创建默认值
    word_count: defaultdict[str, int] = defaultdict(int)
    text: str = "hello world hello python"
    for word in text.split():
        word_count[word] += 1

    # 分组
    students: List[Tuple[str, str]] = [('Alice', 'A'), ('Bob', 'B'), ('Charlie', 'A')]
    grade_groups: defaultdict[str, List[str]] = defaultdict(list)
    for name, grade in students:
        grade_groups[grade].append(name)

    # Counter: 计数器
    letters: Counter[str] = Counter("hello world")
    most_common: List[Tuple[str, int]] = letters.most_common(3)

    print(f"单词计数: {dict(word_count)}")
    print(f"成绩分组: {dict(grade_groups)}")
    print(f"字母计数: {letters}")
    print(f"最常见: {most_common}")


# ============= 12. 生成器表达式 =============
def demo_generators() -> None:
    """生成器：内存高效的迭代"""

    # 生成器表达式：()而不是[]
    squares_gen: Generator[int, None, None] = (x ** 2 for x in range(1000000))

    # 生成器函数
    def fibonacci() -> Generator[int, None, None]:
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    # 使用生成器
    fib_gen = fibonacci()
    first_10_fib: List[int] = [next(fib_gen) for _ in range(10)]

    print(f"前10个斐波那契数: {first_10_fib}")


# ============= 13. with语句 - 上下文管理器 =============
def demo_context_manager() -> None:
    """with语句：资源管理"""

    # 文件操作（自动关闭）
    filename: str = "/Users/hutong/Code/PycharmProjects/python_interesting/data/example.txt"

    # 写文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Hello, Python!")

    # 读文件
    with open(filename, 'r', encoding='utf-8') as f:
        content: str = f.read()

    print(f"文件内容: {content}")


# ============= 14. 切片的高级用法 =============
def demo_slicing() -> None:
    """切片：强大的序列操作"""
    data: List[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 基本切片
    first_five: List[int] = data[:5]
    last_five: List[int] = data[-5:]
    middle: List[int] = data[2:8]

    # 步长切片
    every_second: List[int] = data[::2]
    reverse: List[int] = data[::-1]

    # 字符串切片
    text: str = "Hello, World!"
    reversed_text: str = text[::-1]

    print(f"前五个: {first_five}")
    print(f"每隔一个: {every_second}")
    print(f"反转: {reverse}")
    print(f"反转文本: {reversed_text}")


# ============= 15. 异常处理的优雅写法 =============
def demo_exception_handling() -> None:
    """异常处理：EAFP原则"""

    # EAFP: Easier to Ask for Forgiveness than Permission
    data: Dict[str, Any] = {'name': 'Alice', 'age': 25}

    try:
        # 尝试获取可能不存在的键
        email: str = data['email']
    except KeyError:
        email = "未提供邮箱"

    # 更Pythonic的方式
    email_pythonic: str = data.get('email', '未提供邮箱')

    # 多异常处理
    def safe_divide(a: float, b: float) -> Optional[float]:
        try:
            return a / b
        except (ZeroDivisionError, TypeError) as e:
            print(f"计算错误: {e}")
            return None

    print(f"邮箱: {email}")
    print(f"Pythonic邮箱: {email_pythonic}")
    safe_divide(1, 0)


# ============= 16. 装饰器基础 =============
def demo_decorators() -> None:
    """装饰器：函数的增强"""

    def timer_decorator(func):
        import time
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} 执行时间: {end - start:.4f}秒")
            return result

        return wrapper

    @timer_decorator
    def slow_function() -> str:
        import time
        time.sleep(1)
        return "完成"

    result: str = slow_function()
    print(f"结果: {result}")


# ============= 主函数：运行所有示例 =============
def main() -> None:
    """运行所有示例"""
    demos = [
        ("enumerate示例", demo_enumerate),
        ("zip示例", demo_zip),
        ("列表推导式", demo_list_comprehensions),
        ("字典集合推导式", demo_dict_set_comprehensions),
        ("解包操作", demo_unpacking),
        ("三元运算符", demo_ternary_operator),
        ("Lambda函数", demo_lambda),
        ("函数式编程", demo_functional_programming),
        ("any和all", demo_any_all),
        ("collections模块", demo_collections),
        ("生成器", demo_generators),
        ("切片操作", demo_slicing),
        ("异常处理", demo_exception_handling),
        ("装饰器", demo_decorators),
    ]

    for title, demo_func in demos:
        print(f"\n{'=' * 20} {title} {'=' * 20}")
        demo_func()

    # 演示args和kwargs
    print(f"\n{'=' * 20} args和kwargs示例 {'=' * 20}")
    demo_args_kwargs(1, 2, 3, name="Alice", age=25)
    print(flexible_function("必需", 1, 2, 3, extra="额外", info="信息"))


if __name__ == '__main__':
    main()
