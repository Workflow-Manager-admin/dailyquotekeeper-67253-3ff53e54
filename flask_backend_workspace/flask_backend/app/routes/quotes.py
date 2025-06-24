from flask import Blueprint, render_template, request, redirect, url_for

# Initialize Blueprint for quotes routes
quotes_bp = Blueprint('quotes', __name__, url_prefix='')

# In-memory storage for quotes
quotes_storage = []


# PUBLIC_INTERFACE
@quotes_bp.route('/', methods=['GET'])
def home():
    """Render the homepage with the quote input form."""
    return render_template('home.html')


# PUBLIC_INTERFACE
@quotes_bp.route('/add', methods=['POST'])
def add_quote():
    """Process the submitted quote and store it in the in-memory list."""
    text = request.form.get('quote')
    if text and text.strip():
        quotes_storage.append(text.strip())
    return redirect(url_for('quotes.view_quotes'))


# PUBLIC_INTERFACE
@quotes_bp.route('/quotes', methods=['GET'])
def view_quotes():
    """Display all saved quotes as a simple HTML page."""
    return render_template('quotes.html', quotes=quotes_storage)
