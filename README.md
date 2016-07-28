# txmo-backend
Its is a simple web service that provides restful API written in Flask with Postgres as database. Click this link to see the live demo.
>[https://taxumo-flask.herokuapp.com](https://taxumo-flask.herokuapp.com)
If you see a message like **Not Found**, its okay because its not supposed to display anything other than its exposed APIs.

## List of API
### [company/](https://taxumo-flask.herokuapp.com/api/v1/company/)
Company holds details like tin, address, etc. which is essential in every transaction.
| Method | Description |
| --- | --- |
| get | List all companies |
| post | Add company |

For post request, here is an example json:
```
{
  "name": "Jollibee",
  "address": "Market Market, Bonifacio Global City, Taguig",
  "tin": "123-345-345-123"
}
```
### [transaction/](https://taxumo-flask.herokuapp.com/api/v1/transaction/)
Transaction contains basic details about the purchase.
| Method | Description |
| --- | --- |
| get | List all transactions |
| post | Add transaction |
For post request, here is an example json:
```
{
  "company_id": 1,
  "amount": 111,
  "date": "01-01-2016",
  "type": "expense"
}
```
Initially, this is how i set it up.  Eventually il add more fields as i understood the project needs further.

## TODOs
- [ ] Improve project structure
- [ ] Add validation on fields
- [ ] Add authentication
- [ ] Setup on AWS