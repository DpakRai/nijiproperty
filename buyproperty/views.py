from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets

from buyproperty.serializers import HouseSerializer
from buyproperty.models import HouseImage, House
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib import messages

from django.contrib.auth import get_user_model
from buyproperty.forms import CommentForm


User = get_user_model()

#api view
class HouseViewSets(viewsets.ModelViewSet):
   # Writing the viewsets for the WishHouse 
   queryset = House.objects.all()
   serializer_class = HouseSerializer
   permission_classes = [IsAuthenticatedOrReadOnly]


#django view
@login_required
def create_house_info(request):


    if request.method == 'POST':
        data = request.POST
        buyer = request.user

        house = House()

        house.buyer = buyer
        house.title = data.get('title')
        house.descrption = data.get('descrption')
        house.location = data.get('location')
        house.is_for = data['is-for']

        if data['land_area'] != '':
            house.land_area = data.get('land_area')
        if data['floor_area'] != '':
            house.floor_area = data.get('floor_area')
        if data['bedroom'] != '':
            house.bedroom = data.get('bedroom')
        if data['bathroom'] != '':
            house.bathroom = data.get('bathroom')

        if data['livingroom'] != '':
            house.livingroom = data.get('livingroom')
        if data['kitchen'] != '':
            house.kitchen = data.get('kitchen')
        if data['room_details'] != '':
            house.room_details = data.get('room_details')
        if data['furnished_condition'] != '':
            house.furnished_condition = data.get('furnished_condition')

        if data['built_year'] != '':
            house.built_year = data.get('built_year')
        if data['parking_sapce'] != '':
            house.parking_sapce = data.get('parking_sapce')
        if data['garden'] != '':
            house.garden = data.get('garden')
        if data['house_facing'] != '':
            house.house_facing = data.get('house_facing')
            
        if data['road_size'] != '':
            house.road_size = data.get('road_size')
        if data['road_condition'] != '':
            house.road_condition = data.get('road_condition')
        if data['water_facilities'] != '':
            house.water_facilities = data.get('water_facilities')
        if data['sewage_facilties'] != '':
            house.sewage_facilties = data.get('sewage_facilties')

        house.save()

        images = request.FILES.getlist('images')

        
        for image in images:
            house_image = HouseImage.objects.create(house =house, image=image)
            house_image.save()

        messages.success(request, 'House Info is successfully added')
        return HttpResponseRedirect('/')

    return render(request, 'buyproperty/add_house_info.html')



def house_list(request):
    houses = House.objects.all()
    template = 'buyproperty/house_list.html'
    return render(request, template, {'houses': houses})


def house_detail(request, id):
    template_name = 'buyproperty/house_detail.html'
    house = get_object_or_404(House, id=id)
    comments = house.house_comments.filter(active=True, reply_of=None)
    replies = house.house_comments.filter(active=True).exclude(reply_of=None)
    comment_form = CommentForm() 

    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                cmnt_id = request.POST.get('reply', '')
                if cmnt_id:
                    new_reply = comment_form.save(commit=False)
                    new_reply.house = house
                    new_reply.commented_by = request.user
                    new_reply.reply_of = house.house_comments.get(id=cmnt_id)
                    new_reply.save()
                    messages.success(request, 'Your reply is awaiting moderation!')
                else:
                    new_comment = comment_form.save(commit=False)
                    new_comment.house = house
                    new_comment.commented_by = request.user
                    new_comment.save()
                    messages.success(request, 'Your comment is awaiting moderation!')
            comment_form = CommentForm()
        else:
            messages.warning(request, 'You have to login to comment!')
            return redirect('login')

    return render(request, template_name, {'house': house,
                                           'comments': comments,
                                           'comment_form': comment_form,
                                           'replies': replies})