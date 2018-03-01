"""bga_database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path

from payroll import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('employer/<str:slug>/', views.EmployerView.as_view(), name='employer'),
    path('person/<str:slug>/', views.person, name='person'),
    path('entity-lookup/', views.entity_lookup, name='entity-lookup'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('<int:error_code>', views.error, name='error'),
]


if settings.DEBUG:
    from django.conf.urls import include, url

    import debug_toolbar

    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
