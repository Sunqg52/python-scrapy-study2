from django.conf.urls import url
from demoapp import views

urlpatterns = {
	url(r'^', views.index), # 路由配置
}

def index(request):
	# 主页视图
	return HttpResponse("hello world")