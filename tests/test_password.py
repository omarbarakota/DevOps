import pytest
import string
from main import app

@pytest.fixture

def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_generate_password(client):
    response = client.get('/generate_password')
    
    assert response.status_code == 200
    
    # Check if the response contains the generated password
    password = response.data.decode('utf-8')
    
    # Assuming the password is enclosed in a specific HTML element
    # e.g., <p id="generated-password">{{ password }}</p>
    start_index = password.find('<div class="password">')
    end_index = password.find('</div>', start_index)
    generated_password = password[start_index:end_index]
    #generated_password=(Mid_Pass + '<p><div class="password">')
    # Verify the length of the password
    #print(generated_password)
    #assert len(generated_password) == 12

    # Verify the password contains at least one letter, one digit, and one punctuation character
    assert any(c.isalpha() for c in generated_password)
    assert any(c.isdigit() for c in generated_password)
    ##assert any(c in string.punctuation for c in generated_password)


#test_generate_password(app.test_client())
