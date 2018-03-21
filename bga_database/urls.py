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

from data_import import views as import_views
from payroll import views as payroll_views


urlpatterns = [
    # client
    path('', payroll_views.index, name='home'),
    path('employer/<str:slug>/', payroll_views.EmployerView.as_view(), name='employer'),
    path('person/<str:slug>/', payroll_views.person, name='person'),
    path('entity-lookup/', payroll_views.entity_lookup, name='entity-lookup'),
    path('search/', payroll_views.SearchView.as_view(), name='search'),
    path('<int:error_code>', payroll_views.error, name='error'),

    # admin
    path('admin/', admin.site.urls),
    path('upload-source-file/', import_views.SourceFileHook.as_view(), name='upload-source-file'),
    path('upload/', import_views.StandardizedDataUpload.as_view(), name='upload'),
]


if settings.DEBUG:
    from django.conf.urls import include, url

    import debug_toolbar

    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
