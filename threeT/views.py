from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice, UserChoice, Type

from django.http import JsonResponse
from django.views.decorators.http import require_POST

def reset_quiz(request):
    # 세션에 저장된 사용자의 선택을 초기화
    request.session['user_choices'] = []
    # 퀴즈의 첫 페이지로 리다이렉트하지 않고 성공 응답을 반환
    return JsonResponse({'success': True})


def get_next_question(request, question_id):
    next_question = Question.objects.filter(id__gt=question_id).first()
    if next_question is not None:
        choices = next_question.choice_set.all()
        response = {
            'question_text': next_question.question_text,
            'choices': [choice.choice_text for choice in choices],
            'next_question_id': next_question.id  # 다음 문제의 ID를 반환
        }
    else:
        response = {'question_text': '', 'choices': [], 'next_question_id': None}
    return JsonResponse(response)

def get_previous_question(request, question_id):
    previous_question = Question.objects.filter(id__lt=question_id).last()
    if previous_question is not None:
        choices = previous_question.choice_set.all()
        response = {
            'question_text': previous_question.question_text,
            'choices': [choice.choice_text for choice in choices],
            'previous_question_id': previous_question.id  # 이전 문제의 ID를 반환
        }
    else:
        response = {'question_text': '', 'choices': [], 'previous_question_id': None}
    return JsonResponse(response)


from django.shortcuts import render
from .models import Question


def quiz(request):
    questions = Question.objects.all()
    context = []
    for question in questions:
        context.append({
            'variable': question.question_text,
            'logo_url': question.question_logo.url if question.question_logo else None,
        })
        # print(context)
    return render(request, 'threeT/quiz.html', {'questions': context})

@require_POST
def save_choice(request):
    choice = request.POST.get('choice')
    if choice is not None:
        # 사용자의 선택을 세션에 저장
        user_choices = request.session.get('user_choices', [])
        user_choices.append(int(choice))
        request.session['user_choices'] = user_choices
        return JsonResponse({'status': 'success'})
    else:
        # 올바른 선택이 아닌 경우 오류 응답
        return JsonResponse({'status': 'error'}, status=400)


def review_page(request):
    # 사용자의 선택을 가져옵니다.
    user_choices = request.session.get('user_choices', [])
    question_text_list = [f'{i}번' for i in range(1, len(user_choices) + 1)]

    user_choices_text_list = list(zip(question_text_list, user_choices))

    # 각 유형별 점수를 저장할 딕셔너리를 초기화합니다.
    scores = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'P': 0, 'J': 0}

    # 매핑 로직을 수정합니다.
    answer_string = 'EEII/EEI/EIE/JPJ/SNSN/NNSS/TFTF/SNS/TFTF/JPJP/FFT/PPJJ'
    answer_list = answer_string.split('/')

    try:
        # 매핑 로직
        for question, choice in user_choices_text_list:
            question_index = int(question[:-1]) - 1
            if question_index < len(answer_list) and (choice - 1) < len(answer_list[question_index]):
                type_char = answer_list[question_index][choice - 1]
                scores[type_char] += 1
            else:
                # 범위를 벗어난 경우에 대한 처리
                pass
    except IndexError as e:
        # 인덱스 오류 처리
        print("Index error occurred:", e)
        # 적절한 오류 응답 반환
    # 결과 계산
    result = ('E' if scores['E'] >= scores['I'] else 'I') + \
             ('S' if scores['S'] >= scores['N'] else 'N') + \
             ('T' if scores['T'] >= scores['F'] else 'F') + \
             ('P' if scores['P'] >= scores['J'] else 'J')

    # 결과에 따른 타입 객체 가져오기
    try:
        # type_obj = Type.objects.get(result=result)
        type_obj = Type.objects.filter(result=result).first()

    except Type.DoesNotExist:
        type_obj = None

    return render(request, 'threeT/review_page.html', {
        'user_choices_text_list': user_choices_text_list,
        'scores': scores,
        'result': result,
        'type_obj': type_obj,
    })

from django.http import HttpResponse

def Ads(request):
    return HttpResponse("google.com, pub-8675980791052309, DIRECT, f08c47fec0942fa0")