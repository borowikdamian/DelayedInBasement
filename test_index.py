import unittest

class TestDelayedInBasementHTML(unittest.TestCase):

    def setUp(self):
        self.html_template = '''<!Doctype html>
<html lang="pl">
    <head>
        <meta charset="utf-8"/>
        <meta name="description" content="Page with posts, comments, albums and pictures." />
        <meta name="keywords" content="posts, comments, albums, pictures" />
        <title>DelayedInBasement</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="{{ url_for('css', filename='css/style.css') }}">
    </head>
    <body>
        <main>
            <form action="/posty" method="POST">
                <input id="text" type="text" name="searchbox">
                <button type = "submit" id="button" for="text" >Sumbit!</button>
            </form>
            
        </main>
    </body>
</html>'''

    def tearDown(self):
        print("Zakończono test.")
 
    def test_input_element(self):
        expected_input_type = "text"
        expected_input_name = "searchbox"
        input_element = f'<input id="text" type="{expected_input_type}" name="{expected_input_name}">'
        self.assertIn(input_element, self.html_template)
        print("Test sprawdzający element input zakończony.")

    def test_button_element(self):
        expected_button_type = "submit"
        expected_button_text = "Sumbit!"
        button_element = f'<button type = "{expected_button_type}" id="button" for="text" >{expected_button_text}</button>'
        self.assertIn(button_element, self.html_template)
        print("Test sprawdzający element button zakończony.")

    def test_form_element(self):
        expected_form_action = "/posty"
        expected_form_method = "POST"
        form_element = f'<form action="{expected_form_action}" method="{expected_form_method}">'
        self.assertIn(form_element, self.html_template)
        print("Test sprawdzający element formularza zakończony.")
        

if __name__ =='__main__':
    unittest.main(exit=False)
 