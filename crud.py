import boto3
# This file was used to perfrom CRUD operations on our database for tetsing purposes. CRUD Meaning: CRUD is an acronym that comes from the world of computer programming and refers to the four functions that are considered necessary to implement a persistent storage application: create, read, update and delete.
db = boto3.resource('dynamodb', region_name='us-east-2')
table = db.Table('signuptable')

# get item
response = table.get_item(Key={'email': 'john@doe.com'})
print(response['Item'])

# put item
table.put_item(
    Item={
        'email': 'jane@doe.com',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 25,
    }
)

# update item
table.update_item(
    Key={'email': 'jane@doe.com'},
    UpdateExpression='SET age = :val',
    ExpressionAttributeValues={':val': 16}
)

# delete item
table.delete_item(Key={'email': 'hara@test.com'})


