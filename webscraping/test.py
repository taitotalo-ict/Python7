import requests
from bs4 import BeautifulSoup

# Lukea websivu

# res = requests.get('https://google.com')
# if not res.ok:
#     exit(1)


html_doc = '''
<div>
    <p>This is a paragraph.</p>
    <a href="https://example.com">This is a link.</a>
    <div>
        <span>This is a span inside a div.</span>
    </div>
</div>
'''

# Parse websivu
soup = BeautifulSoup(html_doc, 'html.parser')
