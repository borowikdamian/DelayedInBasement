import unittest

class TestDelayedInBasementHTML(unittest.TestCase):

    def setUp(self):
        with open('templates/posty.html', 'r') as file:
            self.html_template = file.read()

    def tearDown(self):
        print("Zakończono test.")

    def test_title(self):
        expected_title = "DelayedInBasement"
        self.assertIn(expected_title, self.html_template)
        print("Test sprawdzający tytuł zakończony.")

    def test_keywords(self):
        expected_keywords = "posts, comments, albums, pictures"
        self.assertIn(expected_keywords, self.html_template)
        print("Test sprawdzający słowa kluczowe zakończony.")
    
    def test_user(self):
        expected_user = '<p>User:{{x["userId"]}} </p>'
        self.assertIn(expected_user, self.html_template)
        print("Test sprawdzający uzytkownika zakończony.")

    def test_title_section(self):
        expected_title = '<p>Title:{{x["title"]}}</p>'
        self.assertIn(expected_title, self.html_template)
        print("Test sprawdzający tytuł w sekcji zakończony.")
    
    def test_text(self):
        expected_text = '<p>Text:{{x["body"]}}</p>'
        self.assertIn(expected_text, self.html_template)
        print("Test sprawdzający tekst zakończony.")

if __name__ =='__main__':
    unittest.main(exit=False)
 