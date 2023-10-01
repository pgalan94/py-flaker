"""
A simple Flask API that returns paginated random results 
"""
from flask import Flask, request, jsonify
from faker import Faker

app = Flask(__name__)
fake = Faker()

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


@app.route('/api/contacts', methods=['GET'])
def generate_fake_data():
    """API Logic for endpoint: /api/contacts

    Returns a list of randomly generated contacts, based on the 
    "page" GET param. If no paramater is passed, default page 0 is used
    instead.

    GET params:
        page: The seed to randomly generate data. Default 0.
        limit: Number of results to generate. Default 20.
    
    Returns:
        _type_: {
            count: int
            next: int (nº of next page)
            prev: int (nº of previous page)
            results: [] (list of results with size of 'limit' param)
        }
    """
    # Get query parameters
    page = int(request.args.get('page', default=0))
    limit = int(request.args.get('limit', default=20))
    response_data = {
        'count': limit,
        'next': page + 1 if page < 10000 else "",
        'prev': page -1 if page > 0 else 9999 if page > 10000 else "",
        'results': None 
    }

    if page:
        if page > 10000:
            page = 10000
        elif page < 0:
            page = 0
    else:
        page=0
        
    Faker.seed(page)

    data = []
    for _ in range(limit):
        fake_data = {
            'name': fake.name(),
            'email': fake.email(),
            'address': fake.address(),
            'phone_number': fake.phone_number(),
        }
        data.append(fake_data)

    if data:
        response_data['results'] = data

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
