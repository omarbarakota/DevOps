import pytest
from io import BytesIO
import base64 
from main import app
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_generate_qr_code(client):
    test_text = "Test QR Code"
    response = client.post('/generate', data={'text': test_text})
    
    assert response.status_code == 200
    assert test_text in response.data.decode('utf-8')

    # Check if a QR code image is included in the response
    start_index = response.data.decode('utf-8').find('data:image/png;base64,') + len('data:image/png;base64,')
    end_index = response.data.decode('utf-8').find('"', start_index)
    qr_img_base64 = response.data.decode('utf-8')[start_index:end_index]

    # Decode the base64 string to ensure it's a valid PNG image
    qr_img_bytes = base64.b64decode(qr_img_base64)
    img = BytesIO(qr_img_bytes)
    
    assert img.read(8) == b'\x89PNG\r\n\x1a\n'  # Check for PNG file signature

#test_generate_qr_code(app.test_client())