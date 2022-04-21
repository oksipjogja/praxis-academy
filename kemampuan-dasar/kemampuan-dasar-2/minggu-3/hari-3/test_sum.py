assert sum([1,2,3]) == 6    # should be 6
# # nilai True tidak muncul peringatan AssertionError
# assert sum([1,1,1,]) == 6 # should be 6
# AssertionError

def test_sum():
    assert sum([1,2,3]) == 6, 'Should be 6'
if __name__ == '__main__':
    test_sum()
    print("Everything passed")
# apabila dibuka di terminal sesuai direktori file ini berada, ketika dipanggil akan muncul 'Everything passed'

def test_sum():
    assert sum([1,2,3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1,2,2)) == 6, "Should be 6"
if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")
