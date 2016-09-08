from django.shortcuts import render

quizzes = [
	
	{
		"quiz_number":1,
		"name": "Klassiska böcker",
		"description": "Hur bra kan du dina klassiker?"
	},

	{
		"quiz_number": 2,
		"name": "Största lagen",
		"description": "Kan du dina lag?"
	},

	{
		"quiz_number": 3,
		"name": "Världens mest kända hackare",
		"description": "Kan du dina lag?"
	}

]

def startpage(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/startpage.html", context)

def quiz(request):
	return render (request, "quiz/quiz.html")

def question(request):
	return render(request, "quiz/question.html")

def completed(request):
	return render(request, "quiz/completed.html")
