# API
    admin/ 
    api/v1/upload/ [name='upload'] - POST method   
    api/v1/files/ [name='files'] - GET method    

## File model
id - BigAutoField  
file - FileField  
uploaded_at - DateTimeField  
processed - BooleanField  


GET method - http://78.24.222.126/api/v1/files/  
POST method - http://78.24.222.126/api/v1/upload/  