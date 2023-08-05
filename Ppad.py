import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser,font,filedialog,messagebox as mbox
import os

main_application = tk.Tk()
main_application.geometry('800x500')
main_application.title('Prashank Text Edditer')
main_application.wm_iconbitmap('icon.ico')

############################################## Main Menu #####################################################
# ------------------------------&&&&&&&&&&&&& End Main Menu &&&&&&&&&&&&&&&-----------------------------------
main_menu = tk.Menu(main_application)

# File icons
new_icons = tk.PhotoImage(file='icons2/new.png')
open_icons = tk.PhotoImage(file='icons2/open.png')
save_icons = tk.PhotoImage(file='icons2/save.png')
save_as_icons = tk.PhotoImage(file='icons2/save_as.png')
exit_icons = tk.PhotoImage(file='icons2/exit.png')


file = tk.Menu(main_menu,tearoff=False)


# Edit

edit = tk.Menu(main_menu,tearoff=False)
cut_icon = tk.PhotoImage(file=r'icons2\cut.png')
copy_icon = tk.PhotoImage(file=r'icons2\copy.png')
paste_icon = tk.PhotoImage(file=r'icons2\paste.png')
clear_all_icon = tk.PhotoImage(file=r'icons2\clear_all.png')
find_icon = tk.PhotoImage(file=r'icons2\find.png')




# View Icons

view = tk.Menu(main_menu,tearoff=False)
tool_bar_icon = tk.PhotoImage(file=r'icons2\tool_bar.png')
status_bar_icon = tk.PhotoImage(file=r'icons2\status_bar.png')




# Colour Theme

color_theme = tk.Menu(main_menu,tearoff=False)
light_default_icon = tk.PhotoImage(file=r'icons2\light_default.png')
light_plus_icon = tk.PhotoImage(file=r'icons2\light_plus.png')
dark_icon = tk.PhotoImage(file=r'icons2\dark.png')
red_icon = tk.PhotoImage(file=r'icons2\red.png')
monokai_icon = tk.PhotoImage(file=r'icons2\monokai.png')
night_blue_icon = tk.PhotoImage(file=r'icons2\night_blue.png')


theme_choice = tk.StringVar()
color_icons = (light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)

color_dict = {
    "Light default" : ('#000000','#ffffff'),      
    "Light Plus" : ('#474747','#e0e0e0'),
    "Dark" : ('#c4c4c4','#2d2d2d'),
    "Red" : ('#2d2d2d','#ffe8e8'),
    "Monokai" : ('#d3b774','#474747'),
    'Night Blue' : ('#ededed','#6b9dc2')
    }
# first color is text and other is background color


# color_theme.add_checkbutton(label='Light Default Icon',image=light_default_icon,compound=tk.LEFT,accelerator='')

# cascade
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color',menu=color_theme)



############################################## Toolbar ####################################################
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar,width=30,textvariable=font_family,state="readonly")
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar,width=14,textvariable=size_var,state="readonly")
font_size['values'] = tuple(range(8,80,2))
font_size.current(2)
font_size.grid(row=0,column=1,padx=5)


####bold button 
bold_icon = tk.PhotoImage(file=r"icons2\bold.png")
bold_btn = ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

####italic button
italic_icon = tk.PhotoImage(file=r"icons2\italic.png")
italic_btn = ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

####under line button
under_line_icon = tk.PhotoImage(file=r"icons2\underline.png")
under_line_btn = ttk.Button(tool_bar,image=under_line_icon)
under_line_btn.grid(row=0,column=4,padx=5)

####font color button
font_color_icon = tk.PhotoImage(file=r"icons2\font_color.png")
font_color_btn = ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

####align left 
align_left_icon = tk.PhotoImage(file=r"icons2\align_left.png")
align_left_btn = ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

####align center
align_center_icon = tk.PhotoImage(file=r"icons2\align_center.png")
align_center_btn = ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)

####align right
align_right_icon = tk.PhotoImage(file=r"icons2\align_right.png")
align_right_btn = ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)

# -----------------------------&&&&&&&&&&&&& End Toolbar &&&&&&&&&&&&&&&-----------------------------------


############################################## Text Editor ####################################################
text_edditer = tk.Text(main_application)
text_edditer.config(wrap='word',relief=tk.FLAT)
text_edditer.focus_set()        # sercure on the text editer

scroll_bar = tk.Scrollbar(main_application)
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_edditer.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_edditer.yview)
text_edditer.config(yscrollcommand=scroll_bar.set)

#### font size and font families functionality
current_font_family = "Arial"
current_font_size = 12
def change_font(main_aplication):
    global current_font_family
    global current_font_size
    current_font_family = font_family.get()
    current_font_size = font_size.get()
    text_edditer.configure(font=(current_font_family,current_font_size))
font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_font)
text_edditer.configure(font=(current_font_family,current_font_size))


#### button functionality
# print(tk.font.Font(font=text_edditer["font"]).actual())

##Bold button factionalities
def change_bold():
    text_property = tk.font.Font(font=text_edditer['font'])
    if text_property.actual()['weight'] == 'normal':
        text_edditer.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_edditer.configure(font=(current_font_family,current_font_size,"normal"))

bold_btn.configure(command=change_bold)

##Italic button functionality
def change_italic():
    text_property = tk.font.Font(font=text_edditer['font'])
    if text_property.actual()['slant'] == 'roman':
        text_edditer.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_edditer.configure(font=(current_font_family,current_font_size,"roman"))

italic_btn.configure(command=change_italic)

## underline button functionality
def change_underline():
    text_property = tk.font.Font(font=text_edditer['font'])
    if text_property.actual()['underline'] == 0:
        text_edditer.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline'] == 1:
        text_edditer.configure(font=(current_font_family,current_font_size,'normal'))
under_line_btn.configure(command=change_underline)

## font color factionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    # print(color_var)# [1] index is hexa color
    text_edditer.configure(foreground=color_var[1])   # you can also use 'fg' instead of foreground
font_color_btn.configure(command=change_font_color)

### align functionality

## align left
def align_left():
    text_contant = text_edditer.get(1.0,'end')
    text_edditer.tag_config('left',justify=tk.LEFT)
    text_edditer.delete(1.0,tk.END)
    text_edditer.insert(tk.INSERT,text_contant,'lEFT')
align_left_btn.configure(command=align_left)

def align_center():
    text_contant = text_edditer.get(1.0,'end')
    text_edditer.tag_config('center',justify=tk.CENTER)
    text_edditer.delete(1.0,tk.END)
    text_edditer.insert(tk.INSERT,text_contant,'center')
align_center_btn.configure(command=align_center)

def align_right():
    text_contant = text_edditer.get(1.0,'end')
    text_edditer.tag_config('right',justify=tk.RIGHT)
    text_edditer.delete(1.0,tk.END)
    text_edditer.insert(tk.INSERT,text_contant,'right')
align_right_btn.configure(command=align_right)
# -----------------------------&&&&&&&&&&&&& End Text Editor &&&&&&&&&&&&&&&-----------------------------------



############################################# Main Status ####################################################
status_bar = ttk.Label(main_application,text="STATUS BAR")
status_bar.pack(side=tk.BOTTOM)

text_change = False
def changed(event=None):
    global text_change
    if text_edditer.edit_modified():
        text_change = True
        word = len(text_edditer.get(1.0,'end-1c').split())
        # character = len(text_edditer.get(1.0,'end-1c'))
        character = len(text_edditer.get(1.0,'end-1c').replace(' ','')) # for avoiding space
        status_bar.config(text=(f"Character : {character} words : {word}"))
    text_edditer.edit_modified(False)
text_edditer.bind('<<Modified>>',changed)

# ----------------------------&&&&&&&&&&&&& End Main Status &&&&&&&&&&&&&&&-----------------------------------



############################################# Main Fuctionality################################################
## variable
url = ''

## New functionality
def new_file(event=None):
    global url
    url=''
    text_edditer.delete(1.0,tk.END)

####file commond 
file.add_command(label='New',image=new_icons,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)

# Open functionality
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File',"*.txt"),('All File','*.*')))
    try:
        with open(url,'r') as fr :
            text_edditer.delete(1.0,tk.END)
            text_edditer.insert(1.0,fr.read())
    except FileNotFoundError:
        return mbox.showerror('Error','File Not Found Error')
    except:
        return mbox.showerror('Error',"File support Error")
    main_application.title(os.path.basename(url))

file.add_command(label='Open',image=open_icons,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)

## Save functionality
def save_file(event=None):
    global url
    try:
        if url:
            contant = text_edditer.get(1.0,tk.END)
            # contant = str(text_edditer.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(contant)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension=".txt",filetypes=(('Text File',"*.txt"),('All File',"*.*")))
            contant2 = text_edditer.get(1.0,tk.END)
            url.write(contant2)
            url.close()
    except:
        return


file.add_command(label='Save',image=save_icons,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)

## Save as functionality

def save_as_file (event=None):
    global url
    try:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(("All File",'*.*'),("Text File,",'*.txt')))
        contant=text_edditer.get(1.0,tk.END)
        url.write(contant)
        url.close()
    except:
        return mbox.showerror("Error","Unexpected Error")

file.add_command(label='Save as',image=save_as_icons,compound=tk.LEFT,accelerator='Alt+S',command=save_as_file)

## Exit Functionality
def exit_func(event=None):
    global url,text_change
    try:
        if text_change:
            m_box = mbox.askyesnocancel("Warning","Do you want save it?")
            if m_box is True:
                if url:
                    contant = text_edditer.get(1.0,tk.END)
                    with open(url,'w',encoding="uft-8") as fw:
                        fw.write(contant)
                        
                else:
                    contant2 = text_edditer.get(1.0,tk.END)
                    url = filedialog.askopenfile(mode='w',defaultextension=".txt",filetypes=(("Text File","*.txt"),("All File",'*.*')))
                    contant=text_edditer.get(1.0,tk.END)
                    url.write(contant2)
                    url.close()
            elif m_box == False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return


file.add_command(label='Exit',image=exit_icons,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_func)

####Edit commend
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_edditer.event_generate('<Control x>'))
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text_edditer.event_generate('<Control c>'))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_edditer.event_generate('<Control v>'))
def clear_all(event=None):
    text_edditer.delete(1.0,tk.END)

edit.add_command(label='Clear_all',image=clear_all_icon,compound=tk.LEFT,accelerator='Alt+X',command=clear_all)
# edit.add_command(label='Clear_all',image=clear_all_icon,compound=tk.LEFT,accelerator='Alt+X',command=lambda:text_edditer.delete(1.0,tk.END))

## Find Functionaality
def find_func(event=None):
    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x200+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    def find(event=0):
        word = find_input.get()
        text_edditer.tag_remove('match',1.0,tk.END)
        matches = 0
        if word:
            start_pos = 1.0
            while True:
                start_pos = text_edditer.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text_edditer.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_edditer.tag_config('match',foreground='red',background='yellow')


    ## replace functionality
    def replace(event=0):
        word = find_input.get()
        replace_text = replace_input.get()
        contant = text_edditer.get(1.0,tk.END)
        text_edditer.delete(1.0,tk.END)
        new_contant = contant.replace(word,replace_text)
        text_edditer.insert(1.0,new_contant)


    ## Fame
    find_fame = ttk.LabelFrame(find_dialogue,text="Find/Replace")
    find_fame.pack(pady=40)
    # find_fame.pack(padx=40)

    ## label
    text_find_label = ttk.Label(find_fame,text='Find')
    text_replace_label = ttk.Label(find_fame,text="Replace")

    ## Entry Box
    find_input = ttk.Entry(find_fame,width=30)
    replace_input = ttk.Entry(find_fame,width=30)

    ## button
    find_btn = ttk.Button(find_fame,text='Find',command=find)
    replace_btn = ttk.Button(find_fame,text="Replace",command=replace)

    ## Grid label
    text_find_label.grid(row=0,column=0,sticky=tk.W,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,sticky=tk.W,padx=4,pady=4)

    ## G Entry box
    find_input.grid(row=0,column=1,sticky=tk.W,padx=4,pady=4)
    replace_input.grid(row=1,column=1,sticky=tk.W,padx=4,pady=4)

    ## G button 
    find_btn.grid(row=0,column=2,padx=8,pady=8)
    replace_btn.grid(row=1,column=2,padx=8,pady=8)

    find_dialogue.mainloop()


edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_func)

#####View command
show_tool_bar=tk.BooleanVar()
show_tool_bar.set(True)
show_status_bar=tk.BooleanVar()
show_status_bar.set(True)

def hide_tool_bar(event=None):
    global show_tool_bar
    if show_tool_bar:
        tool_bar.pack_forget()
        show_tool_bar=False
    else:
        status_bar.pack_forget()
        text_edditer.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_edditer.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM,fill=tk.X)
        show_tool_bar=True

def hide_status_bar(event=None):
    global show_status_bar
    if show_status_bar:
        status_bar.pack_forget()
        show_status_bar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_status_bar=True

view.add_checkbutton(label='Tool Bar',image=tool_bar_icon,onvalue=True,offvalue=False,variable=show_tool_bar,compound=tk.LEFT,accelerator="Alt+l",command=hide_tool_bar)
view.add_checkbutton(label='Status Bar',image=status_bar_icon,onvalue=1,offvalue=0,variable=show_status_bar,compound=tk.LEFT,accelerator='Alt+m',command=hide_status_bar)

####Color command
## change theme functionality 
def change_theme(event=None):
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0],color_tuple[1]
    # print(color_tuple)
    text_edditer.configure(background=bg_color,fg=fg_color)

count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count+=1
# ----------------------------&&&&&&&&&&&&& End Main Functionality &&&&&&&&&&&&&&&-----------------------------------


main_application.config(menu=main_menu)

main_application.bind("<Control-n>",new_file)
main_application.bind('<Control-o>',open_file)
main_application.bind('<Control-s>',save_file)
main_application.bind('<Alt-s>',save_as_file)
main_application.bind('<Control-q>',exit_func)
main_application.bind('<Control-f>',find_func)
main_application.bind('<Alt-x>',clear_all)
main_application.bind('<Alt-m>',hide_status_bar)
main_application.bind('<Alt-l>',hide_tool_bar)

main_application.mainloop()