from src.infra.migration.migrate import Migrate
from src.infra.driver.driver import Driver

def test_driver_connection():
    driver = Driver()
    Migrate(driver=driver).perform()
    
    sql="""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE  table_schema = 'public'
            AND    table_name   = 'users'
        );
    """
    error, success = driver.execute(sql=sql, returning="first")
    
    assert error is None
    assert "exists" in success.keys()
    assert success.get("exists") is True