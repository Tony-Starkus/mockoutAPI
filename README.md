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
##### Return
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


## Route
For all posts requests, use this route:  
`<url>/api/v1`  
\<url> is where django server is runing in your machine


## Body
These are the attributes you can pass in the body of the request.

| Attribute Name | Type |  Description  |
| :---           | :--- | :---:          |
|  total_data |  int | Define how many data you want to receive.  |
| fields        | array  | Array of objects. Each object is a field. |


## Building fields
In this section, you see the attributes to build the fields.  
All fields requires 2 attributes:

| Attribute Name | Type |  Description  |
| :---           | :--- | :---:          |
|  field_name |  string | The name of the field.  |
| type        | string  | The type of the field. |

For each type, there is attributes that defines how to build the field data.

### string
| Attribute Name | Type |  Description  |
| :---           | :--- | :---:          |
|  max_length |  integer | Define the string max length. Default is 20. |
| mask        | string   | Define a mask for the string. Use X letter to replace with a random number. Example: XX-X will be something like 35-7.

### int
| Attribute Name | Type |  Description  |
| :---           | :--- | :---:          |
|  range |  string | Define the range of random numbers. Default is "0-100".  |

### cpf
| Attribute Name | Type |  Description  |
| :---           | :--- | :---:          |
|  unique |  boolean | Define if cpf must be unique. Default is false. |
| formated | boolean | Format cpf like XXX.XXX.XXX-XX. Default is false. |

### date
| Attribute Name | Type |  Description  |
| :---           | :--- | :---:          |
|  range |  string | Required. Define the range of generated dates. The format is "Y-m-d Y-m-d". Left date in the format can't be greater than the right date. |


## Frameworks/Bibliotecas
- Django
- Django Rest
- [cpf-generator](https://pypi.org/project/cpf-generator/)
