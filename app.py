"""
A simple Flask API that returns paginated random results 
"""
from flask import Flask, request, jsonify

app = Flask(__name__)
contacts = []  # Store the list of contacts


@app.route('/', methods=['GET'])
def app_routes():
    """
    API Root endpoint. Returns a JSON with all available endpoints.
    """
    routes = {
        '/api/contacts': 'Contact list'
    }
    routes_data = {
        'count': len(routes.keys()),
        'results': routes
    }

    return jsonify(routes_data)

@app.route('/api/contacts', methods=['GET', 'POST'])
def handle_contacts():
    """API Route to handle contacts.
    GET returns a list of contacts
    POST is to create new contacts. Needs a form with name, email and phone fields.

    Returns:
        _type_: JSON
    """
    if request.method == 'POST':
        # Create a new fake contact
        if request.form:
            new_contact = {
                'name': request.form['name'] if request.form['name'] else "",
                'email': request.form['email'] if request.form['email'] else "",
                'phone': request.form['phone'] if request.form['phone'] else ""
            }
            contacts.append(new_contact)

            # Return a response indicating the contact was created
            return jsonify({'message': 'Contact created successfully'})
        return jsonify({'message': 'Form error. Contact was not created.'})

    # Get query parameters
    page = int(request.args.get('page', default=0))
    limit = int(request.args.get('limit', default=20))

    # Calculate the pagination parameters
    total_contacts = len(contacts)
    start_index = page * limit
    end_index = min(start_index + limit, total_contacts)

    # Prepare the response data
    response_data = {
        'count': total_contacts,
        'next': page + 1 if end_index < total_contacts else None,
        'prev': page - 1 if page > 0 else None,
        'results': contacts[start_index:end_index]
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
