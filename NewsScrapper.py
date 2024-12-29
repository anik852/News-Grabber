from tkinter import *
import sqlite3
import webbrowser
import pa_news
import ifq_news


def relode():
    pa_news.latest()
    pa_news.special_news()
    pa_news.politics()
    pa_news.cr_viris()
    pa_news.bangladesh()
    pa_news.world()
    pa_news.business()
    pa_news.opinion()
    pa_news.sports()
    pa_news.entertainment()
    pa_news.chakri()
    pa_news.lifestyle()
    ifq_news.latest_news()
    ifq_news.special_news()
    ifq_news.national()
    ifq_news.country()
    ifq_news.politics()
    ifq_news.world_news()
    ifq_news.sports()
    ifq_news.entertainment()
    ifq_news.business()
    ifq_news.lifestyle()
    ifq_news.tech()
    ifq_news.opinion()
    ifq_news.news()

# First Window


window = Tk()
window.geometry("800x800")
window.title("First Window")
window.config(background="#0a0a0a")

# create 1st frame:
myframe1 = Frame(window, width=700, height=200, bd=2, relief=GROOVE)

# Project Title
label = Label(window,
              text="NEWS GRABBER",
              font=("Arial", 28, "bold"),
              foreground="silver",
              background="black",
              relief=RAISED)
label.place(x=250, y=25)

button2 = Button(window, text="Refresh", fg="black",
                 bg="silver", font=("Arial", 12), command=relode)
button2.place(x=200, y=150)

# Set the Menu initially
menu = StringVar()
menu.set("Select Keyword")
options = [
    "জাতীয়",
    "করোনাভাইরাস",
    "বিশ্ব",
    "বাণিজ্য",
    "রাজনীতি",
    "খেলা",
    "বিনোদন",
    "লাইফস্টাইল",
    "চাকরি",
    "মতামত"
]

# Create a dropdown Menu
drop = OptionMenu(window,
                  menu,
                  *options
                  )
drop.place(x=350, y=150)

national = ["জাতীয়", "সারাদেশ", "রাজধানী", "জেলা", "অপরাধ", "পরিবেশ"]
crv = ["করোনাভাইরাস"]
world = ["বিশ্ব", "রাশিয়া", "ইউক্রেন", "সংঘাত", "ভারত", "পাকিস্তান", "চীন",
         "মধ্যপ্রাচ্য", "এশিয়া", "যুক্তরাষ্ট্র", "ইউরোপ", "আফ্রিকা", "লাতিন আমেরিকা", "ওশেনিয়া"]
business = ["বাণিজ্য", "শেয়ারবাজার", "ব্যাংক", "শিল্প", "অর্থনীতি", "বিশ্ববাণিজ্য",
            "বিশ্লেষণ", "আপনার টাকা", "উদ্যোক্তা", "করপোরেট সংবাদ", "বাজেট ২০২২-২৩"]
politics = ["রাজনীতি"]
sports = ["খেলা", "ক্রিকেট", "ফুটবল", "অন্য খেলা",
          "টেনিস", "সাক্ষাৎকার", "ফটো ফিচার"]
entertainment = ["টেলিভিশন", "ওটিটি", "ঢালিউড", "টালিউড", "বলিউড",
                 "হলিউড", "বিশ্ব চলচ্চিত্র", "গান", "নাটক", "আলাপন", "বিনোদন", "টেক"]
lifestyle = ["ভ্রমণ", "সম্পর্ক", "সুস্থতা", "রাশি", "ফ্যাশন", "স্টাইল", "রূপচর্চা",
             "গৃহসজ্জা", "রসনা", "কেনাকাটা", "লাইফস্টাইল", "জীবনযাপন", "ভিন্নচোখে"]
chakri = ["চাকরি", "খবর", "নিয়োগ", "পরামর্শ", "সাক্ষাৎকার"]
openion = ["মতামত", "সম্পাদকীয়", "কলাম",
           "সাক্ষাৎকার", "স্মরণ", "প্রতিক্রিয়া", "চিঠি"]


def ol(link):
    webbrowser.open(link)


def load_data():
    keyword = menu.get()
    if keyword in national:
        keys = national
    elif keyword in crv:
        keys = crv
    elif keyword in world:
        keys = world
    elif keyword in business:
        keys = business
    elif keyword in politics:
        keys = politics
    elif keyword in sports:
        keys = sports
    elif keyword in entertainment:
        keys = entertainment
    elif keyword in lifestyle:
        keys = lifestyle
    elif keyword in chakri:
        keys = chakri
    elif keyword in openion:
        keys = openion
    #print(keys)
    conn = sqlite3.connect('News_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM news")
    items = c.fetchall()

    labels = []
    bt = []
    # create 2nd frame:
    myframe2 = Frame(window,
                     width=700,
                     height=800,
                     bd=2,
                     relief=GROOVE
                     )
    #myframe2.place(x=100, y=250)
    myframe2.pack(padx=0, pady=250, expand=True)

    # Add a canvas to the frame
    canvas = Canvas(myframe2,
                    width=600,
                    height=700
                    )
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Add a scrollbar to the frame
    scrollbar = Scrollbar(myframe2, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the canvas to work with the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")))

    # Create another frame inside the canvas to hold the buttons and labels
    inner_frame = Frame(canvas,
                        height=450,
                        width=450,
                        bg='blue',
                        bd=2,
                        relief=GROOVE
                        )
    canvas.create_window((50, 50), window=inner_frame, anchor="nw")

    i = 0
    for item in items:
        title = item[1]
        key = item[2]
        link = item[0]
        if key in keys:
            labels.append(Label(inner_frame,
                                text=title
                                ))
            labels[i].pack()
            bt.append(Button(inner_frame,
                             text="read more",
                             fg="black",
                             font=("Arial", 10),
                             command=lambda item=item: ol(link)
                             ))
            #bt[i].place(x=480, y=20+(30*i))
            bt[i].pack()
            i = i+1
        else:
            continue
    conn.commit()
    conn.close()


# Button to search
button1 = Button(window, text="Search", fg="black",
                 bg="silver", font=("Arial", 12), command=load_data)
button1.place(x=500, y=150)


myframe1.place(x=50, y=10)


# Function For Second Window
def secondWindow():
    def relode():
        pa_news.latest()
        pa_news.special_news()
        pa_news.politics()
        pa_news.cr_viris()
        pa_news.bangladesh()
        pa_news.world()
        pa_news.business()
        pa_news.opinion()
        pa_news.sports()
        pa_news.entertainment()
        pa_news.chakri()
        pa_news.lifestyle()
        ifq_news.latest_news()
        ifq_news.special_news()
        ifq_news.national()
        ifq_news.country()
        ifq_news.politics()
        ifq_news.world_news()
        ifq_news.sports()
        ifq_news.entertainment()
        ifq_news.business()
        ifq_news.lifestyle()
        ifq_news.tech()
        ifq_news.opinion()
        ifq_news.news()
    window.destroy()
    secondWindow = Tk()  # Secondone object is new window
    secondWindow.geometry("800x800")
    secondWindow.title("First Window")
    secondWindow.config(background="#0a0a0a")

    # create 1st frame:
    secframe1 = Frame(secondWindow, width=700, height=200, bd=2, relief=GROOVE)

    # Project Title
    seclabel = Label(secondWindow,
                    text="NEWS GRABBER",
                    font=("Arial", 28, "bold"),
                    foreground="silver",
                    background="black",
                    relief=RAISED)
    seclabel.place(x=250, y=25)

    secbutton2 = Button(secondWindow, text="Refresh", fg="black",
                        bg="silver", font=("Arial", 12), command=relode)
    secbutton2.place(x=200, y=150)

# Set the Menu initially
    secmenu = StringVar()
    secmenu.set("Select Keyword")
    secoptions = [
        "জাতীয়",
        "করোনাভাইরাস",
        "বিশ্ব",
        "বাণিজ্য",
        "রাজনীতি",
        "খেলা",
        "বিনোদন",
        "লাইফস্টাইল",
        "চাকরি",
        "মতামত"
    ]

# Create a dropdown Menu
    secdrop = OptionMenu(secondWindow,
                        secmenu,
                        *secoptions
                        )
    secdrop.place(x=350, y=150)

    national = ["জাতীয়", "সারাদেশ", "রাজধানী", "জেলা", "অপরাধ", "পরিবেশ"]
    crv = ["করোনাভাইরাস"]
    world = ["বিশ্ব", "রাশিয়া", "ইউক্রেন", "সংঘাত", "ভারত", "পাকিস্তান", "চীন",
         "মধ্যপ্রাচ্য", "এশিয়া", "যুক্তরাষ্ট্র", "ইউরোপ", "আফ্রিকা", "লাতিন আমেরিকা", "ওশেনিয়া"]
    business = ["বাণিজ্য", "শেয়ারবাজার", "ব্যাংক", "শিল্প", "অর্থনীতি", "বিশ্ববাণিজ্য",
            "বিশ্লেষণ", "আপনার টাকা", "উদ্যোক্তা", "করপোরেট সংবাদ", "বাজেট ২০২২-২৩"]
    politics = ["রাজনীতি"]
    sports = ["খেলা", "ক্রিকেট", "ফুটবল", "অন্য খেলা",
          "টেনিস", "সাক্ষাৎকার", "ফটো ফিচার"]
    entertainment = ["টেলিভিশন", "ওটিটি", "ঢালিউড", "টালিউড", "বলিউড",
                 "হলিউড", "বিশ্ব চলচ্চিত্র", "গান", "নাটক", "আলাপন", "বিনোদন", "টেক"]
    lifestyle = ["ভ্রমণ", "সম্পর্ক", "সুস্থতা", "রাশি", "ফ্যাশন", "স্টাইল", "রূপচর্চা",
             "গৃহসজ্জা", "রসনা", "কেনাকাটা", "লাইফস্টাইল", "জীবনযাপন", "ভিন্নচোখে"]
    chakri = ["চাকরি", "খবর", "নিয়োগ", "পরামর্শ", "সাক্ষাৎকার"]
    openion = ["মতামত", "সম্পাদকীয়", "কলাম",
           "সাক্ষাৎকার", "স্মরণ", "প্রতিক্রিয়া", "চিঠি"]


    def ol(link):
        webbrowser.open(link)


    def load_data():
        keyword = secmenu.get()
        if keyword in national:
            keys = national
        elif keyword in crv:
            keys = crv
        elif keyword in world:
            keys = world
        elif keyword in business:
            keys = business
        elif keyword in politics:
            keys = politics
        elif keyword in sports:
            keys = sports
        elif keyword in entertainment:
            keys = entertainment
        elif keyword in lifestyle:
            keys = lifestyle
        elif keyword in chakri:
            keys = chakri
        elif keyword in openion:
            keys = openion
        #print(keys)
        conn = sqlite3.connect('News_data.db')
        c = conn.cursor()
        c.execute("SELECT * FROM news")
        items = c.fetchall()

        seclabels = []
        secbt = []
    # create 2nd frame:
        secmyframe2 = Frame(secondWindow,
                        width=700,
                        height=800,
                        bd=2,
                        relief=GROOVE
                        )
    #myframe2.place(x=100, y=250)
        secmyframe2.pack(padx=100, pady=250, expand=True)

    # Add a canvas to the frame
        seccanvas = Canvas(secmyframe2,
                    width=600,
                    height=700
                    )
        seccanvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Add a scrollbar to the frame
        secscrollbar = Scrollbar(secmyframe2, orient=VERTICAL, command=seccanvas.yview)
        secscrollbar.pack(side=RIGHT, fill=Y)

    # Configure the canvas to work with the scrollbar
        seccanvas.configure(yscrollcommand=secscrollbar.set)
        seccanvas.bind('<Configure>', lambda e: seccanvas.configure(scrollregion=seccanvas.bbox("all")))

    # Create another frame inside the canvas to hold the buttons and labels
        secinner_frame = Frame(seccanvas,
                        height=450,
                        width=450,
                        bg='blue',
                        bd=2,
                        relief=GROOVE
                        )
        seccanvas.create_window((50, 50), window=secinner_frame, anchor="nw")

        i = 0
        for item in items:
            title = item[1]
            key = item[2]
            link = item[0]
            if key in keys:
                seclabels.append(Label(secinner_frame,
                                 text=title
                                    ))
                seclabels[i].pack()
                secbt.append(Button(secinner_frame,
                                text="read more",
                                fg="black",
                                font=("Arial", 10),
                                command=lambda item=item: ol(link)
                                ))
            #bt[i].place(x=480, y=20+(30*i))
                secbt[i].pack()
                i = i+1
            else:
                continue
        conn.commit()
        conn.close()


# Button to search
    secbutton1 = Button(secondWindow, text="Search", fg="black",
                    bg="silver", font=("Arial", 12), command=load_data)
    secbutton1.place(x=500, y=150)

    secframe1.place(x=50, y=10)
    # Button to search
    secbuttonRepeat = Button(secondWindow, text="Try Again", fg="black",
                 bg="silver", font=("Arial", 12), command=lambda rep = NONE: secondWindow )
    secbuttonRepeat.place(x=350, y=210)
    secondWindow()
    #secondWindow.mainloop() #Execute second window
    
# Button to search again
buttonRepeat = Button(window, text="Try Again", fg="black",
                 bg="silver", font=("Arial", 12), command=secondWindow)
buttonRepeat.place(x=350, y=210)
window.mainloop()  # Execute first window
