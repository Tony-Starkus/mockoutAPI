# mockoutAPI
MokoutAPI is a fake API that build data according to your needs.
It's useful when you need many data to test your frontend layout, like tables and responsiviness.

##### Example 1 - Get users data
```
{
 "total_data": 2,
 "fields": [
   {
    "field_name": "name",
    "type": "string",
    "max_length": 20
    },
   {
     "field_name": "age",
     "type": "int",
     "range": "1-90"
   },
   {
     "field_name": "cpf",
     "type": "cpf",
     "formated": true,
     "unique": true
   },
   {
     "field_name": "born_date",
     "type": "date",
     "range": "1980-01-01 2021-01-01"
   },
   {
     "field_name": "phone",
     "type": "string",
     "mask": "(XX) XXXXX-XXXX"
   }
 ]
}
```
#####Return
```
{
  "data": [
    {
      "name": "h sec",
      "age": 24,
      "cpf": "684.990.839-19",
      "born_date": "1991-03-29",
      "phone": "(70) 62213-8425"
    },
    {
      "name": "dfrfqpk dhou sheubp",
      "age": 72,
      "cpf": "086.889.631-42",
      "born_date": "2015-03-29",
      "phone": "(19) 00175-9447"
    }
  ]
}
```

### Instalation
1. Clone the repository.
2. Create a python virtual env
3. Install the packages  
`$ pip install -r requirements.txt`
4. Run Django server  
`$ python manage.py runserver`


## Routes
For all posts requests, use this route:  
`<url>/api/v1`  
<url> is where django server is runing in your machine


## Build fields
In this section, you see the attributes to build the fields.  
All fields requires 2 attributes:  
field_name: name of the field  
type: the type of the field.  
<br>
For each type, there is attributes that defines how to build the field data.

### String
| Attribute Name | Type |  Description  |
| :---           | :--- | :---:          |
|  max_length |  integer | Define the string max length. Default is 20 |

## Frameworks/Bibliotecas
- Django
- Django Rest
- [cpf-generator](https://pypi.org/project/cpf-generator/)
