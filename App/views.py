from django.shortcuts import render
import datetime
def Home( request ) :
    contextdata =  {
        'id' : 1,
        'name' : 'Baker',
        'value' : [1,2,3,4,5],
        'lst' : ['a','b','c'],
        'val' : 123456784,
        'a' : "i'm Baker",
        'date' : datetime.datetime.now(),
        'str' : "",
        'data' :  [   
                { 'name' : 'Baker', 'age' : 23 },
                { 'name' : 'Sujon', 'age' : 20 },
                { 'name' : 'Faker', 'age' : 21 }
            ],
        'lststr' : 'I am a student of phitron',
        'lstint' : 1235332,
        'blog_date' : datetime.datetime.now(),
        'unlist' : ['Noakhali',['Feni','Cumilla'],'Dhaka',['Magura',['Dhaka','Bhola']]],
        'emptystr' : "",
        'description' : 'Once Upon a time there was a farmer in a village',
        'num_messages' : 5

    }
    
    return render(request,'home.html',contextdata)
