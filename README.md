# GET - /v1/categories

200 - Ok
```json
{
    "previousPage": null,
    "currentPage": 0,
    "nextPage": null,
    "last": true,
    "totalPages": 1,
    "totalItems": 2,
    "maxItemsPerPage": 50,
    "totalItemsPage": 2,
    "items": [
        {
            "id": 1,
            "name": "Humanas"
        },
        {
            "id": 2,
            "name": "Biológicas"
        }
    ]
}
```

# GET - /v1/colleges

200 - Ok 
```json
{
    "previousPage": null,
    "currentPage": 0,
    "nextPage": null,
    "last": true,
    "totalPages": 1,
    "totalItems": 2,
    "maxItemsPerPage": 50,
    "totalItemsPage": 2,
    "items": [
        {
            "id": 2,
            "name": "Universidade Nove de Julho (UNINOVE)",
            "city": "São Paulo"
        },
        {
            "id": 3,
            "name": "Universidade São Francisco (USF)",
            "city": "Campinas"
        }
    ]
}
```


# GET - /v1/colleges/{collegeId}

200 - Ok
```json
{
    "previousPage": null,
    "currentPage": 0,
    "nextPage": 1,
    "last": false,
    "totalPages": 3,
    "totalItems": 114,
    "maxItemsPerPage": 50,
    "totalItemsPage": 50,
    "items": [
        {
            "id": 3,
            "semesters": 10,
            "period": "Noturno",
            "modality": "Presencial",
            "course": "Direito",
            "category": "Humanas"
        },
        {
            "id": 2,
            "semesters": 10,
            "period": "Matutino",
            "modality": "Presencial",
            "course": "Direito",
            "category": "Humanas"
        },
        {
            "id": 5,
            "semesters": 10,
            "period": "Noturno",
            "modality": "Presencial",
            "course": "Filosofia",
            "category": "Humanas"
        }
    ]
}
```

# POST - /v1/login

200 - Ok
```json
{
    "name": "Jose Carlos",
    "email": "xxxy@gmail.com",
    "phone": "11979922135",
    "income": 1500.0,
    "document": "96166886004",
    "person_type": "Aluno",
    "birth_date": "01/06/1994",
    "id": 5,
    "sponsor_id": 3,
    "course_college_id": 17,
    "description": "Minha Primeira faculdade também"
}
```

404 - Not Found
```json
{
    "message": "Not found"
}
```

# POST - /v1/students

201 - Created
```json
{
    "name": "Marcos Souza",
    "email": "marquinhos@gmail.com",
    "phone": "11979922135",
    "income": 1500.0,
    "document": "37434431040",
    "person_type": "Aluno",
    "birth_date": "01/06/1994",
    "id": 7,
    "description": "Desejo me formar"
}
```

422 - Unprocessable Entity
```json
{
    "message": "There is already a student registered with this document"
}
```


# GET - /v1/students

200 - Ok
```json
{
    "previousPage": null,
    "currentPage": 0,
    "nextPage": null,
    "last": true,
    "totalPages": 1,
    "totalItems": 1,
    "maxItemsPerPage": 50,
    "totalItemsPage": 1,
    "items": [
        {
            "id": 5,
            "sponsor_id": 3,
            "course_college_id": 17,
            "description": "Minha Primeira faculdade também",
            "name": "Jose Carlos",
            "email": "xxxy@gmail.com",
            "phone": "11979922135",
            "income": 1500.0,
            "birth_date": "01/06/1994"
        }
    ]
}
```


# GET - /v1/students/{studentId}

200 - Ok
```json
{
    "id": 5,
    "sponsor_id": 3,
    "course_college_id": 17,
    "description": "Querendo cursar minha primeira faculdade"
}
```

404 - Not Found
```json
{
    "error": "Student Not Found"
}
```


# DELETE - /v1/students/{studentId}

200 - Ok
```json
{
    "id": 7,
    "sponsor_id": null,
    "course_college_id": 177,
    "description": "Desejo me formar"
}
```

404 - Not Found
```json
{
    "error": "Student Not Found"
}
```


# PUT - /v1/students/{studentId}?courseId={courseId}

200 - Ok
```json
{
    "id": 7,
    "sponsor_id": null,
    "course_college_id": 177,
    "description": "Desejo me formar"
}
```

404 - Not Found
```json
{
    "error": "Student Not Found"
}
```


# POST - /v1/sponsors 

Payload de envio:

```json
{
    "name": "Dave Mustaine",
    "password": "Megadeth@1983",
    "contact": {
        "email": "daveMu@gmail.com",
        "cellphoneNumber": "11937584488"
    },
    "monthlyIncome": 201850.65,
    "documentNumber": "63858197017",
    "birthDate": "1962-04-23",
    "reasonsWhy": "Gosto de apoiar estudantes"
}
```


201 - Created
```json
{
    "id": 4,
    "reasons": "Gosto de apoiar estudantes"
}
```

409 - Conflict
```json
{
    "error": "Sponsor Already Exists"
}
```

# DELETE - /v1/sponsors/{sponsorId}
204 - No Content

404 - Not Found
```json
{
    "message": "Sponsor not found"
}
```

422 - Unprocessable Entity
```json
{
    "message": "This sponsor has students"
}
```


# PUT - /v1/sponsors/{sponsorId}/sponsorize?studentId={studentId}

200 - Ok
```json
{
    "id": 8,
    "sponsor_id": 10,
    "course_college_id": null,
    "description": "Desejo me formar"
}
```

404 - Not Found
```json
{
    "error": "Sponsor Not Found"
}
```

404 - Not Found
```json
{
    "error": "Student Not Found"
}
```

409 - Conflict
```json
{
    "error": "Student Already Sponsored"
}
```
