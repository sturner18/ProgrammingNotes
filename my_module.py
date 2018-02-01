period = "B"

# parameters are inputs to the function
# they are assigned locally

def hello(name):
    '''
    says hello to the name
    :param name:
    :return:
    '''
    print("Hello there,", name + ".")

def product_sum(n1, n2):
    '''
    returns product and Sum of two numbers
    :param n1:
    :param n2:
    :return product, sum:
    '''
    product = n1 * n2
    sum = n1+ n2
    return product, sum

print(product_sum(4,5))