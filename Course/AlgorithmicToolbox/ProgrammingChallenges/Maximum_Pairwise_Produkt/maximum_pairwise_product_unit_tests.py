""" python3
Type here ersetzen
"""

def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    type here


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
    
"""
dont goes

"/home/pi/PycharmProjects/Algorithmic Toolbox/.idea/VirtualEnvironment/bin/python" /home/pi/pycharm/plugins/python-ce/helpers/pycharm/_jb_unittest_runner.py --path "/home/pi/PycharmProjects/Algorithmic Toolbox/Programming Challenges/Maximum Pairwise Product/maximum_pairwise_product_unit_tests.py"
Testing started at 6:19 AM ...
Traceback (most recent call last):
  File "/home/pi/pycharm/plugins/python-ce/helpers/pycharm/_jb_unittest_runner.py", line 35, in <module>
    sys.exit(main(argv=args, module=None, testRunner=unittestpy.TeamcityTestRunner, buffer=not JB_DISABLE_BUFFERING))
  File "/usr/lib/python3.7/unittest/main.py", line 100, in __init__
    self.parseArgs(argv)
  File "/usr/lib/python3.7/unittest/main.py", line 147, in parseArgs
    self.createTests()
Launching unittests with arguments python -m unittest /home/pi/PycharmProjects/Algorithmic Toolbox/Programming Challenges/Maximum Pairwise Product/maximum_pairwise_product_unit_tests.py in /home/pi/PycharmProjects/Algorithmic Toolbox/Programming Challenges/Maximum Pairwise Product
  File "/usr/lib/python3.7/unittest/main.py", line 159, in createTests

    self.module)
  File "/usr/lib/python3.7/unittest/loader.py", line 220, in loadTestsFromNames
    suites = [self.loadTestsFromName(name, module) for name in names]
  File "/usr/lib/python3.7/unittest/loader.py", line 220, in <listcomp>
    suites = [self.loadTestsFromName(name, module) for name in names]
  File "/usr/lib/python3.7/unittest/loader.py", line 154, in loadTestsFromName
    module = __import__(module_name)
  File "/home/pi/PycharmProjects/Algorithmic Toolbox/Programming Challenges/Maximum Pairwise Product/maximum_pairwise_product_unit_tests.py", line 10
    type here
            ^
SyntaxError: invalid syntax

Process finished with exit code 1

Empty suite
"""