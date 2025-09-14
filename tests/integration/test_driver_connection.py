from src.infra.driver.driver import Driver

def test_driver_connection():
    driver = Driver()
    error, success = driver.execute(sql="SELECT NOW()", returning="first")
    
    assert error is None
    assert success.get('now') is not None