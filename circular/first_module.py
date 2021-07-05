# from circular.second_module import second_module_test
# from circular.second_module import second_module_test


def first_module_test():
    print('first_module_test func')


def test():
    # import circular.second_module
    import circular.second_module as sm
    sm.second_module_test()
    print("test")


if __name__ == '__main__':
    # first_module_test()
    test()

