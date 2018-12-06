from django.http import JsonResponse

from blog.tasks import CourseTask


def do(request):
    # 执行异步
    print('start do request')
    CourseTask.delay()
    print('end do request')
    return JsonResponse({'result': 'ok'})