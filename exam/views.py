import json

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from exam.models import Question, Answer, Chapter, Unit, Knowledge_point
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class Normal_ShowView(View):
    def get(self, request):
        Question_data = Question.objects.filter(pk=3)
        # 获取主键为1的题目的题目干
        Answer_data0 = Answer.objects.filter(question_id=3)[0]
        Answer_data1 = Answer.objects.filter(question_id=3)[1]
        Answer_data2 = Answer.objects.filter(question_id=3)[2]
        Answer_data3 = Answer.objects.filter(question_id=3)[3]
        Answer_data = [Answer_data0, Answer_data1, Answer_data2, Answer_data3]
        # 获取与主键相同的题目的答案 分四个地方存储 放在数组传入前端

        return render(request, 'test.html', {'Question_data': Question_data, 'Answer_data': Answer_data})


class ShowQuestionsView(View):
    def get(self, request):
        Chapter_data = Chapter.objects.all()
        Question_data = Question.objects.all()
        Answer_data_loop = Answer.objects.all()
        print(Question_data)
        # 获取主键为1的题目的题目干
        Answer_data0 = Answer.objects.filter(question_id=3)[0]
        Answer_data1 = Answer.objects.filter(question_id=3)[1]
        Answer_data2 = Answer.objects.filter(question_id=3)[2]
        Answer_data3 = Answer.objects.filter(question_id=3)[3]
        Answer_data = [Answer_data0, Answer_data1, Answer_data2, Answer_data3]
        # 获取与主键相同的题目的答案 分四个地方存储 放在数组传入前端

        return render(request, 'test.html',
                      {'Question_data': Question_data, 'Answer_data': Answer_data, 'Chapter_data': Chapter_data,
                       'Answer_data_loop': Answer_data_loop})

    def post(self, request):
        return HttpResponse('失败')


@csrf_exempt
def get_question(request):
    print(request.POST)
    return HttpResponse('0')


class ShowChapterView(View):  # 展示常规学习界面
    def get(self, request):
        Chapter_data = Chapter.objects.all()
        Unit_data = Unit.objects.all()
        # print(Chapter_data,Unit_data)
        return render(request, 'show_chapter.html', {'Chapter_data': Chapter_data})


@csrf_exempt
def get_unit_content(request):
    unit_id = request.GET.get('unit_id')
    unit = Unit.objects.get(id=unit_id)

    dada = list(unit.knowledge_point_set.all().values('content'))
    # queryset强转list
    data_v = [kp['content'] for kp in dada]
    print(data_v)

    return JsonResponse(data_v, safe=False)
