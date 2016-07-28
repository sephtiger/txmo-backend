from flask import Flask, request, jsonify
from flask.ext.heroku import Heroku
from flask_restful import Api, Resource
from settings import DevConfig
from models import db, Company, Transaction

app = Flask(__name__)
heroku = Heroku(app)
app.config.from_object(ProdConfig)
db.init_app(app)
api = Api(app)

class CompanyApi(Resource):
   def get(self, id=None):
      if id is None:
         companies = Company.query.all()
         return jsonify([i.serialize for i in companies])

      company = Company.query.get(id)
      if company is None:
         return jsonify(message='Company does not exist')
      else:
         return jsonify(company.serialize)
   def post(self):
      if(Company.exists(request.form['name'])):
         return jsonify(message='Company exists')
      else:
         company = Company()
         company.name = request.form['name']
         company.tin = request.form['tin']
         company.address = request.form['address']
         db.session.add(company)
         db.session.commit()
         return jsonify(company.serialize)

class TransactionApi(Resource):
   def get(self):
      transactions = Transaction.query.all()
      return jsonify([i.serialize for i in transactions])
   def post(self):
      company = Company.query.get(request.form['company_id'])
      if company is None:
         return jsonify(message='Company does not exists')
      transaction = Transaction()
      transaction.company_id  = company.id
      transaction.type = request.form['type']
      transaction.amount = request.form['amount']
      transaction.date = request.form['date']
      db.session.add(transaction)
      db.session.commit()
      return jsonify(transaction.serialize)

API_VERSION = '/api/v1/'
"""Exposed APIs."""
api.add_resource(CompanyApi, API_VERSION + 'company/', API_VERSION + 'company/<int:id>')
api.add_resource(TransactionApi, API_VERSION + 'transaction/')

if __name__ == '__main__':
   app.run(host='0.0.0.0')

