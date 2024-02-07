# py-flaker
A python faker API using Flask

## usage

install with pip install -r requirements.txt
run with python app.py
in another script, run a request to Flask endpoints.

## endpoints

(GET '/': root, list of endpoints)

curl http://127.0.0.1:5000/

(GET '/api/contacts': Query contacts)

curl http://127.0.0.1:5000/api/contacts (doesn't work with ending '/')

(POST '/api/contacts/': Create contact)

    body: {
      "name": optional, 
      "email": optional, 
      "phone": optional
    } # at least one must be present
