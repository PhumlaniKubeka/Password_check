from password import password_is_valid, password_is_ok


def test_password_is_valid():
  
        assert password_is_valid('Tdhjgg1fhj') == True
def test_password_is_ok():
    assert password_is_ok("sfdjsDsas1") == True
        
   