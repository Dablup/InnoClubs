from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from .models import Club, Student, ClubAdmin
from django.http import HttpResponseRedirect


# if user is not logged in => redirect to the auth/
# if user is logged in => show main page
# args['infoFromDb'] = .... means that we add information of all the clubs from database to the args
def main(request):
    args = {}
    if auth.get_user(request).username:
        args['username'] = auth.get_user(request).username
        try:
            args['infoFromDb'] = Club.objects.all()
        except ObjectDoesNotExist:
            args['infoFromDb'] = None
        return render(request, "clubs/main.html", args)
    else:
        return redirect("auth/")


# if user is not logged in => redirect to the auth/
# if user is logged in => show main page
# args['infoFromDb'] = Club.objects.get(club_url=club_url)
# means that we add information of the exactly one club that was accessed
def ClubPage(request, club_url):
    args = {}
    if auth.get_user(request):
        args['user'] = auth.get_user(request)
        args['infoFromDb'] = Club.objects.get(club_url=club_url)

        return render(request, "clubs/pageOfClub.html", args)
    else:
        return redirect('auth/')


def subscribe(request, club_url):
    user = auth.get_user(request)
    club = Club.objects.get(club_url=club_url)
    user.student.subscriptions.add(club)
    return HttpResponseRedirect(reverse('clubPage', args=(club_url,)))  # almost same as redirect


def unsubscribe(request, club_url):
    user = auth.get_user(request)
    club = Club.objects.get(club_url=club_url)
    user.student.subscriptions.remove(club)
    return HttpResponseRedirect(reverse('clubPage', args=(club_url,)))


def administration(request, club_url):
    args = {}
    club = Club.objects.get(club_url=club_url)
    args['user'] = auth.get_user(request)
    args['club'] = club
    args['students'] = Student.objects.filter(subscriptions__club_url=club_url)
    admins_list = []
    for record in club.clubadmin_set.all():
        admins_list.append(record.student)
    args['admins_list'] = admins_list

    return render(request, "clubs/administrationOfClub.html", args)


def addEvent(request, club_url):
    pass
