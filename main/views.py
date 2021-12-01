from django.shortcuts import render
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import ContactForm
from .models import Topic


# Create your views here.
from django.shortcuts import render

def index(request): 
    return render(request, 'main/index.html')
def atomic_models(request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/atomic-models.html', context)
def big_bang (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/big_bang.html', context)
def black_holes (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/black_holes.html', context)
def black_body (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/black-body.html', context)
def bohrs_mod (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/bohrs_mod.html', context)
def brem_rad (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/brem_rad.html', context)
def exp_universe (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/exp_universe.html', context)

def feynman_d (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/feynman-d.html', context)

def galaxies (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/galaxies.html', context)
def heisenberg_uncertainty (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/heisenberg-uncertainty.html', context)

def higgs (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/higgs.html', context)

def pe_effect (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form} 
    return render(request, 'main/pe-effect.html', context)

def q_comp (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/q_comp.html', context)
def q_teleporation (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form} 
    return render(request, 'main/q_teleporation.html', context)

def qc_alg (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/qc_alg.html', context)

def qed (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/qed.html', context)
def ruth_mod (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/ruth_mod.html', context)
def schr_eq (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/schr-eq.html', context)
def shors_alg (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/shors_alg.html', context)
def space_time (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/space-time.html', context)
def standard_model (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form} 
    return render(request, 'main/standard_model.html', context)
def star_form (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/star_form.html', context)
def supernovae (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/supernovae.html', context)
def thermonuclear_fus (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/thermonuclear_fus.html', context)
def turing_machine (request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/turing_machine.html', context)
def q_teleporation(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/q_teleporation.html', context)



def text_field(request):
    return render(request, 'main/text_field.html')

def generator(request):
    return render(request, 'main/generator.html')
def register(request):
    return render(request, 'main/register.html')
def top_menu(request):
    return render(request, 'main/top_menu.html')


def top_menu_no_contact(request):
    return render(request, 'main/top_menu_no_contact.html')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})


def text_algo(request):
    from . import text_blocks
    if request.method=='POST':
        if "analysis" in request.POST:
            text=[]
            weird_list = request.POST["analysis"]
            text.append(weird_list)
        else:
            text=[]
            weird_list='hay'
            text.append(weird_list.split())
        
            

        if ('\t' in text):
            split_input=text.split('\t')
        else:
            split_input=[]
            try:
                while True:
                    if text[a] == '.' and b==3:
                        b=0
                        split_input.append(text[:a+1])
                        text = text[a+1:]
                        print(':))))', text)
                        a=0
                    elif text[a] == '.' and b<3:
                        b+=1
                        a+=1
                    else:
                        a+=1
            except:
                split_input.append(text)
                
        main_blocks=split_input
        dict_block_main={}
        for j in main_blocks:
            name_for_block_main='block'+str(main_blocks.index(j))+'_'+'main'
            dict_block_main[str(name_for_block_main)]=j

        dict_block={}
        list_block=[]
        for paragarph in split_input:


            if('black body' in paragarph):
                list_block.append(str(text_blocks.black_body))
            elif('ultraviolet' or 'x-rays' or 'spectrum' or 'rainbow' in paragarph):
                list_block.append(str(text_blocks.spectrum))
        
            elif('fusion' or 'energy' or 'thermonuclear' or 'reactor' in paragarph):

                list_block.append(str(text_blocks.thermonuclear_fusion))
            else:
                pass
            for i in list_block:
                name_for_block='block'+str(list_block.index(paragarph))+'_'+i
                dict_block[str(name_for_block)]=list_block[i]
            
        print(dict_block_main)
        print(dict_block)

        return render(request, 'main/text_algo_template.html', {'content':[dict_block_main['block1_main'], dict_block['block1_1'], dict_block['block1_2']]})
    else:
        
        return render(request, 'main/index.html')






'''def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/success.html')
        else:
            return render(request, 'main/error.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, __self__, context)'''

        


def search_results(request):
    if request.method=='POST':
        searched_thing=request.POST['searched_thing']
        topics=Topic.objects.filter(name__contains=searched_thing)


        return render(request, 'main/search_results.html', {'searched_thing':searched_thing, 'topics':topics})
    else:
        return render(request, 'main/search_results.html', {'searched_thing': 'fuck'})