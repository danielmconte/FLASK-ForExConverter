from app import app
from unittest import TestCase

class ConversionTests(TestCase):
    def test_convert_form(self):
        """Tests Post Request """
        with app.test_client() as client:
            res = client.post('/next', data = {'convert_from':'USD', 'convert_to': 'USD', 'amount':'1'})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h2>The result is US$1.0</h2>', html)
    
    def test_redirect(self):
        """Tests redirects"""
        with app.test_client() as client:
            res = client.get('/home')

            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, 'http://localhost/')

    def test_redirect_followed(self):
         """Tests redirects follow through to form"""
        with app.test_client() as client:
            res = client.get('/home', follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h2>Currency Converter</h2>', html)
