#view functions go here and will be for each of the things I have.
from django.http import HttpResponse, JsonResponse, QueryDict #JsonResponse builds JSON resp object 
from django.shortcuts import render
from django.template import loader #what does this do...?
from .models import Meal
from django.views.decorators.csrf import csrf_exempt
# def home(request):
#     return render(request, ''){

#     } 
def index(request):
    # latest_meals_list = Meal.objects.order_by('pub_date') #order by meal owner and saves in this array
    # template = loader.get_template('restaurant/index.html')
    # context ={
    #     'meals': latest_meals_list, 
    # }
    # return HttpResponse(template.render(context,request))
    return render(request,'restaurant/index.html', {
        'meal': Meal.objects.all()
    })

def meals(request):
    if request.method == 'POST':
        ml = request.POST['meal-owner']
        new_ml = Meal(meal_owner=ml)
        new_ml.save()
        return JsonResponse({
        'id': new_ml.id,
        'meal_owner' : new_ml.meal_owner
        })
    if request.method == 'GET':
        return JsonResponse({
        'meals': list(Meal.objects.values()) #list of dictionaries, dictionaries being key values eg name: Sawda. A list of them being like a Json Payload 
        })

@csrf_exempt
def meals_change(request):
    if request.method =='PUT':
        id = int(QueryDict(request.body).get('id'))
        new_name = QueryDict(request.body).get('name')
        meal_ch = Meal.objects.get(id = id)
        meal_ch.meal_owner=new_name
        print(meal_ch)
        # meal_ch.name = new_name
        meal_ch.save() 
        response = JsonResponse({
            'result': 'success'
        })
        response.status_code = 200
        return response

    if request.method == 'DELETE':
        id = int(QueryDict(request.body).get('id'))
        # print(QueryDict(request.body))
        
        meal_del.delete()
        response = JsonResponse({
            'result': 'success'
        })
        response.status_code = 200
        return response
    
      


