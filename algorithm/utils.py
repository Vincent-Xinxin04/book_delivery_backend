import math
from django.utils import timezone
from .models import Order

# 计算两点 (x1,y1) 与 (x2,y2) 的距离（简单欧氏距离，仅示例，实际看坐标类型）
def calculate_distance(x1, y1, x2, y2):  
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# 推荐算法主逻辑
def recommend_orders(volunteer_x, volunteer_y, distance_threshold=None):  
    all_orders = Order.objects.all()
    order_distance_list = []
    for order in all_orders:
        distance = calculate_distance(volunteer_x, volunteer_y, order.x, order.y)
        # 若有距离范围约束，先过滤
        if distance_threshold is not None and distance > distance_threshold:  
            continue
        order_distance_list.append({
            "order_id": order.order_id,
            "distance": distance,
            "created_time": order.created_time
        })
    # 先按距离升序，距离相同按创建时间升序（即更早创建排前面，也可按需调整降序）
    order_distance_list.sort(key=lambda x: (x["distance"], x["created_time"]))  
    # 提取需要的返回格式，这里简单返回列表套字典
    return [{"order_id": item["order_id"], "distance": item["distance"]} for item in order_distance_list]