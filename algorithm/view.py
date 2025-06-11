from django.http import JsonResponse
from .utils import recommend_orders

def get_recommended_orders(request):
    # 从请求中获取志愿者坐标，这里假设前端传 query 参数，实际也可放请求体等
    volunteer_x = request.GET.get("volunteer_x", type=float)  
    volunteer_y = request.GET.get("volunteer_y", type=float)  
    # 假设前端可传距离阈值，无则默认不限制（实际可根据业务定默认值）
    distance_threshold = request.GET.get("distance_threshold", type=float)  

    result = recommend_orders(volunteer_x, volunteer_y, distance_threshold)
    return JsonResponse({"recommended_orders": result})
