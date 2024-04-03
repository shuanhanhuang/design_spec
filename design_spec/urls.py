"""
URL configuration for design_spec project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
# from specapp.views import homeIndex,homePost,homeDelete,fileUpload,comparePost,compareIndex,compareEdit,orderView,orderPost,orderEdit,\
#                             tableBOMPost,tableBOMIndex,tableBOMDelete,tableBOMDelete2,tablespecPost,tablespecView,tablespecEdit
from specapp.views import designIndex,designPost,designDelete,fileUpload,comparePost,compareIndex,compareEdit,tablespecPost,tablespecView,tablespecEdit,designEdit,designView,\
    render_pdf_view,download_workbook
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',designIndex),
    path('render_pdf_view/<str:cNumber>/',render_pdf_view,name = 'render_pdf_view'),
    path('download_workbook/<str:cNumber>/',download_workbook,name = 'download_workbook'),

    path('designIndex/',designIndex),
    path('designPost/',designPost),
    path('designDelete/<int:id>/',designDelete),
    path('designEdit/<int:id>/<str:mode>',designEdit),
    path('designView/<int:id>/',designView),

    path('fileUpload/',fileUpload),

    path('comparePost/<str:cNumber>/',comparePost),
    path('compareIndex/<str:cNumber>/',compareIndex),
    path('compareEdit/<str:cNumber>/<int:id>/<str:mode>',compareEdit),

    path('tablespecPost/<str:cNumber>/',tablespecPost),
    path('tablespecView/<str:cNumber>/',tablespecView),
    path('tablespecEdit/<str:cNumber>/<str:mode>',tablespecEdit)

    # path('orderPost/<int:id>/<str:cNumber>/',orderPost),
    # path('orderView/<int:id>/<str:cNumber>/',orderView),
    # path('orderEdit/<int:id>/<str:cNumber>/<str:mode>',orderEdit),
    # path('tableBOMPost/<str:cNumber>/',tableBOMPost),
    # path('tableBOMIndex/<str:cNumber>/',tableBOMIndex),
    # path('tableBOMDelete/<int:id>/<str:cNumber>/',tableBOMDelete),
    # path('tableBOMDelete2/<int:id>/<str:cNumber>/',tableBOMDelete2),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
