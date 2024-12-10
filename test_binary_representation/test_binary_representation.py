
def test_values():
    values_dict = {13.375: '1101.011',
                   0.5: '0.1',
                   0.75: '0.11',
                   1.0: '1.0',
                   0.0: '0.0'}
    
    for value, binary in values_dict.items():
        try:
            assert binary_representation(value) == binary
        except AssertionError:
            print(f'Assertion Error for value {value}')
        else:
            print(f'Test passed for value {value}')
    
def test_name():
    try:
        binary_representation(13.375)
    except Exception as e:
        print("There is not a function named binary_representation")
    else:
        print("Name is True")

def test_var_type(x):
    if not isinstance(x, float):
        raise TypeError("The input must be a float.")
    if not isinstance(binary_representation(x),str):
        raise TypeError("The output must be a string.")
    else:
        print("Var Type is True")


if __name__ == '__main__':
    try:
        test_name()
        test_var_type(1.0)
        test_values()

    except Exception as e:
        print('Test failed {}'.format(e))

    else:
        print('All tests passed')
    
    