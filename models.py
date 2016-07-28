from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Create our database model
class Company(db.Model):
   __tablename__ = "company"
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(120))
   tin = db.Column(db.String(120))
   address = db.Column(db.String(120))

   def __repr__(self):
      return '<Company name %r >' % self.name

   @staticmethod
   def exists(name):
      company = Company.query.filter_by(name=name).one_or_none()
      return company is not None

   @property
   def serialize(self):
      return {
            'id'      : self.id,
            'name'    : self.name,
            'tin'     : self.tin,
            'address' : self.address
      }

class Transaction(db.Model):
   __tablename__ = "transaction"
   id = db.Column(db.Integer, primary_key=True)
   company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
   type = db.Column(db.String(120))
   amount = db.Column(db.Float())
   date = db.Column(db.Date())

   def __repr__(self):
      return '<Transaction with %r >' % self.company.name

   @property
   def serialize(self):
      return {
            'id'         : self.id,
            'company_id' : self.company_id,
            'type'       : self.type,
            'amount'     : self.amount,
            'date'       : self.date
      }
