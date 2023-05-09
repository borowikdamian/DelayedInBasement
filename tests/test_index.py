import unittest


class TestDelayedInBasementHTML(unittest.TestCase):

    def setUp(self):
        
        with open('templates/index.html', 'r') as file:
            self.html_template = file.read()

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
 