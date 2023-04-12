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
                                        <div id="body">
                                            <a href="{{ url_for('index') }}" method="POST">
                                                <img src="{{ url_for('static', filename='powrot.png') }}" alt="Cofnij" width="40px" height="40px">
                                            </a>
                                            <article>
                                                {% for x in posts %}
                                                <section>
                                                    <p>User:{{x["userId"]}} </p>
                                                    <p>Title:{{x["title"]}}</p>
                                                    <p>Text:{{x["body"]}}</p>
                                                    <p>Comments:
                                                        {%for y in comments
                                                            if x["id"] == y["postId"]:%}
                                                            <div id="comment">
                                                            <p>Name:{{y["name"]}} </p>
                                                            <p>email:{{y["email"]}}</p>
                                                            <p>body:{{y["body"]}}</p>
                                                            <hr>
                                                            </div>
                                                        {% endfor %}

                                                    </p>

                                                </section>
                                                {% endfor %}
                                            </article>
                                        </div>
                                    </body>
                                </html>'''

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
 