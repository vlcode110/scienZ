import text_blocks

text='As an Excel MVP, I spectrum had been trying for years to convince Microsoft to add icons to the ribbon for superscript and subscript so we can put black body them on the Quick Access Toolbar (QAT) above the ribbon. Word has suitable icons, so all the Excel development team needed to do was to copy those icons. I got nowhere, however.Microsoft has a new venue to solicit user input for desired features. If a feature request gets 20 votes, it will be looked at. And the more votes it gets after passing this threshold, the higher the priority the idea will receive for implementation. So I urged anyone viewing this thread to take a look at my proposal on Excel UserVoice, and vote for it. Yll have to sign up before you can vote, but the process is painless.'
if ('\t' in text):
    split_input=text.split('\t')
    
else:
    split_input=[]
    try:
        while True:
            if text[a] == '.' and b==2:
                b=0
                split_input.append(text[:a+1])
                text = text[a+1:]
                print(':))))', text)
                a=0
            elif text[a] == '.' and b<2:
                b+=1
                a+=1
            else:
                a+=1
            
            
    except:
        split_input.append(text)
        print(split_input)
                

            

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
        #return render(request, 'main/text_algo_template.html', {'content':[dict_block_main['block1_main'], dict_block['block1_1'], dict_block['block1_2']]})
    
        #return render(request, 'main/index.html')
