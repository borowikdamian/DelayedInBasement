import requests
import unittest
import re

class Tests(unittest.TestCase):

    def test(self):
        response = requests.get('http://localhost:5000/')
        assert response.status_code == 200

        assert '<input id="text" type="text" name="searchbox">' in response.text
        assert '<button type = "submit" id="button" for="text" >Sumbit!</button>' in response.text
        
        response = requests.post('http://localhost:5000/posty', data={"searchbox": 'sunt'})
        assert response.status_code == 200

        pattern = r'<p>Title:.*sunt.*</p>'
        matches = re.findall(pattern, response.text)
        assert len(matches) > 0, 'Nie znaleziono tytułów zawierających frazę "sunt"'
if __name__ == '__main__':
    unittest.main()