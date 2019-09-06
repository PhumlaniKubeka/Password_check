from password import password_is_valid, password_is_ok
def test_pass_larger_than_eight():
        assert password_is_valid('2ujdhjhjhRjkt') == True

def test_lower_case_letter():
        assert password_is_valid('ESKSKKKDKdF') == True

def test_upper_case_letter():
        assert password_is_valid('sfdkgkhdlgk') == True

def  test_atleast_one_number():
        assert password_is_valid('KDSLKFLKDSLKiL1') == True

def test_is_null():
        assert password_is_valid("") == False

def test_password_is_ok():
    assert password_is_ok("sfdjsDsas1") == True
