from django.shortcuts import render
from profiles.models import Profile

# Create your views here.

#@login_required
def seatAlloc(request):
    applns = Profile.objects.filter(rank__gt=0).order_by('rank')
    for obj in applns:
        pref1 = obj.pref1
        pref2 = obj.pref2
        pref3 = obj.pref3
        if pref1.seats>0:
            obj.allotted = pref1
            obj.allotted_pref = 1
            pref1.seats = pref1.seats-1
            pref1.save()
        elif pref2.seats>0:
            obj.allotted = pref2
            obj.allotted_pref = 2
            pref2.seats = pref2.seats-1
            pref2.save()
        elif pref3.seats>0:
            obj.allotted = pref3
            obj.allotted_pref = 3
            pref3.seats = pref3.seats-1
            pref3.save()
        print "hello"
        print obj.allotted
        print obj.allotted_pref
        obj.save()
    return render(request, 'seats_allotted.html')

