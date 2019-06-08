from django.shortcuts import render

# Create your views here.
full_text_list = []
def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    full_text = request.GET['fulltext']
    
    full_text_list.append(full_text)
    word_list = full_text.split()
    
    word_dictionary = {}
    letter_count = 0

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
        letter_count += len(word)
    return render(request, 'wordcount/count.html',{'letter_count':letter_count,'fulltextlist':full_text_list,'fulltext':full_text, 'total':len(word_list), 'dictionary': word_dictionary.items()})

def previous(request):
    for text in full_text_list:
        added_text = text
    return render(request, 'wordcount/previous.html',{'text':added_text})