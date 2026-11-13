# 第一个 Python 程序
import sys
import platform

def main():
    print("你好，VS Code！")
    print(f"Python 版本: {platform.python_version()}")
    print(f"解释器路径: {sys.executable}")
    print(f"运行平台: {platform.system()} {platform.release()}")
    print("-" * 30)
    total = sum(i * i for i in range(1, 11))
    print(f"1 到 10 的平方和 = {total}")

if __name__ == "__main__":
    main()