from collections import OrderedDict
ordered_dict = OrderedDict([('apple', 2), ('orange', 3)])
# The order of 'apple' and 'orange' will be preserved
for key, value in ordered_dict.items():
    print("key: {}, value: {}\n".format(key, value))