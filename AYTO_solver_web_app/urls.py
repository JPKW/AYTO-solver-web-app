from django.conf.urls import include, url
import AYTOSolver.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    url(r'^$', AYTOSolver.views.index, name='index'),
    url(r'^home$', AYTOSolver.views.index, name='home'),
    url(r'^test$', AYTOSolver.views.test, name='test'),
]