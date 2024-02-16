from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse('''
        <script>
            var increas() = function(){
                alert("hello html world)
            }
         </script>
        <button style="background-color:red" onclick="increas()"> hello world </button>
        <br></br>
        <input></input>
        <br></br>
        <select></select>
        


        
        
        

        
                        ''')