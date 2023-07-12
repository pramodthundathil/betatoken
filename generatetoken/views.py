from django.shortcuts import render,redirect
from rest_framework import response
from rest_framework.decorators import api_view
from .models import Call_Tokens
from .serializers import Call_Taken_Serializer

# Create your views here.
@api_view(['GET'])
def Generate_Token(request):
    listtokens = Call_Tokens.objects.all()
    if len(listtokens) != 0:
        mytoken = Call_Tokens.objects.all().last()
        token = Call_Tokens.objects.create(tokens = mytoken.tokens +1)
        token.save()
    else:
        token = Call_Tokens.objects.create(tokens = 1)
        token.save()
    serializer = Call_Taken_Serializer(token,many=False)
    return response.Response(serializer.data)

@api_view(["POST"])
def Clean_Tokens(request):
    tokens = Call_Tokens.objects.all()
    tokens.delete()
    return response.Response("Token Cleaned")

@api_view(["POST"])
def TokenCount(request):
    try:
        lasttoken = Call_Tokens.objects.filter(call_status = False).first()
        token = Call_Tokens.objects.get(id = lasttoken.id)
        token.call_status = True
        token.save()
        print(token.tokens,"0==========================")
        serializer = Call_Taken_Serializer(token,many=False)
        return response.Response(serializer.data)
    except:
        # return response.Response("No more tokens")
        return redirect('Generate_Token')
        
    
