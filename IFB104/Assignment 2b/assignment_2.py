
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 1, 2024.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#  Put your student number here as an integer and your name as a
#  character string:
#
student_number = 1203946
student_name   = 'Thomas McGhee'
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assessment Task 2 Description----------------------------------#
#
#  In this assessment task you will combine your knowledge of Python
#  programming, HTML-style mark-up languages, pattern matching,
#  database management, and Graphical User Interface design to produce
#  a robust, interactive "app" that allows its user to view and save
#  data from multiple online sources.
#
#  See the client's briefings accompanying this file for full
#  details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by a paying
#  "client".  This single template file will be used for all parts,
#  together with some non-Python support files.
#
#--------------------------------------------------------------------#



#-----Set up---------------------------------------------------------#
#
# This section imports standard Python 3 modules sufficient to
# complete this assignment.  Don't change any of the code in this
# section, but you are free to import other Python 3 modules
# to support your solution, provided they are standard ones that
# are already supplied by default as part of a normal Python/IDLE
# installation.
#
# However, you may NOT use any Python modules that need to be
# downloaded and installed separately, such as "Beautiful Soup" or
# "Pillow", because the markers will not have access to such modules
# and will not be able to run your code.  Only modules that are part
# of a standard Python 3 installation may be used.

# A function for exiting the program immediately (renamed
# because "exit" is already a standard Python function).
from sys import exit as abort

# A function for opening a web document given its URL.
# [You WILL need to use this function in your solution,
# either directly or via the "download" function below.]
from urllib.request import urlopen

# Some standard Tkinter functions.  [You WILL need to use
# SOME of these functions in your solution.]  You may also
# import other widgets from the "tkinter" module, provided they
# are standard ones and don't need to be downloaded and installed
# separately.  (NB: Although you can import individual widgets
# from the "tkinter.tkk" module, DON'T import ALL of them
# using a "*" wildcard because the "tkinter.tkk" module
# includes alternative versions of standard widgets
# like "Label" which leads to confusion.  If you want to use
# a widget from the tkinter.ttk module name it explicitly,
# as is done below for the progress bar widget.)
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar

# Functions for finding occurrences of a pattern defined
# via a regular expression.  [You do not necessarily need to
# use these functions in your solution, because the problem
# may be solvable with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.]
from re import *

# A function for displaying a web document in the host
# operating system's default web browser (renamed to
# distinguish it from the built-in "open" function for
# opening local files).  [You WILL need to use this function
# in your solution.]
from webbrowser import open as urldisplay

# All the standard SQLite database functions.  [You WILL need
# to use some of these in your solution.]
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Validity Check-------------------------------------------------#
#
# This section confirms that the student has declared their
# authorship.  You must NOT change any of the code below.
#

if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

#
#--------------------------------------------------------------------#



#-----Supplied Function----------------------------------------------#
#
# Below is a function you can use in your solution if you find it
# helpful.  You are not required to use this function, but it may
# save you some effort.  Feel free to modify the function or copy
# parts of it into your own code.
#

# A function to download and save a web document.  The function
# returns the downloaded document as a character string and
# optionally saves it as a local file.  If the attempted download
# fails, an error message is written to the shell window and the
# special value None is returned.  However, the root cause of the
# problem is not always easy to diagnose, depending on the quality
# of the response returned by the web server, so the error
# messages generated by the function below are indicative only.
#
# Parameters:
# * url - The address of the web page you want to download.
# * target_filename - Name of the file to be saved (if any).
# * filename_extension - Extension for the target file, usually
#      "html" for an HTML document or "xhtml" for an XML
#      document.
# * save_file - A file is saved only if this is True. WARNING:
#      The function will silently overwrite the target file
#      if it already exists!
# * char_set - The character set used by the web page, which is
#      usually Unicode UTF-8, although some web pages use other
#      character sets.
# * incognito - If this parameter is True the Python program will
#      try to hide its identity from the web server. This can
#      sometimes be used to prevent the server from blocking access
#      to Python programs. However we discourage using this
#      option as it is both unreliable and unethical to
#      override the wishes of the web document provider!
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'downloaded_document',
             filename_extension = 'html',
             save_file = True,
             char_set = 'UTF-8',
             incognito = False):

    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception sometimes raised when a web server
    # denies access to a document
    from urllib.error import HTTPError

    # Import an exception raised when a web document cannot
    # be downloaded due to some communication error
    from urllib.error import URLError

    # Open the web document for reading (and make a "best
    # guess" about why if the attempt fails, which may or
    # may not be the correct explanation depending on how
    # well behaved the web server is!)
    try:
        if incognito:
            # Pretend to be a web browser instead of
            # a Python script (not recommended!)
            request = Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; ' + \
                               'rv:91.0; ADSSO) Gecko/20100101 Firefox/91.0')
            print("Warning - Request to server does not reveal client's true identity.")
            print("          Use this option only if absolutely necessary!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError as message: # probably a syntax error
        print(f"\nCannot find requested document '{url}'")
        print(f"Error message was: {message}\n")
        return None
    except HTTPError as message: # possibly an authorisation problem
        print(f"\nAccess denied to document at URL '{url}'")
        print(f"Error message was: {message}\n")
        return None
    except URLError as message: # probably the wrong server address
        print(f"\nCannot access web server at URL '{url}'")
        print(f"Error message was: {message}\n")
        return None
    except Exception as message: # something entirely unexpected
        print("\nSomething went wrong when trying to download " + \
              f"the document at URL '{str(url)}'")
        print(f"Error message was: {message}\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError as message:
        print("\nUnable to decode document from URL " + \
              f"'{url}' as '{char_set}' characters")
        print(f"Error message was: {message}\n")
        return None
    except Exception as message:
        print("\nSomething went wrong when trying to decode " + \
              f"the document from URL '{url}'")
        print(f"Error message was: {message}\n")
        return None

    # Optionally write the contents to a local text file
    # (silently overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(f'{target_filename}.{filename_extension}',
                             'w', encoding = char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print(f"\nUnable to write to file '{target_filename}'")
            print(f"Error message was: {message}\n")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution below.
#
'''

███████╗██████╗░███████╗███████╗  ██████╗░░█████╗░██╗░░░░░███████╗░██████╗████████╗██╗███╗░░██╗███████╗
██╔════╝██╔══██╗██╔════╝██╔════╝  ██╔══██╗██╔══██╗██║░░░░░██╔════╝██╔════╝╚══██╔══╝██║████╗░██║██╔════╝
█████╗░░██████╔╝█████╗░░█████╗░░  ██████╔╝███████║██║░░░░░█████╗░░╚█████╗░░░░██║░░░██║██╔██╗██║█████╗░░
██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░  ██╔═══╝░██╔══██║██║░░░░░██╔══╝░░░╚═══██╗░░░██║░░░██║██║╚████║██╔══╝░░
██║░░░░░██║░░██║███████╗███████╗  ██║░░░░░██║░░██║███████╗███████╗██████╔╝░░░██║░░░██║██║░╚███║███████╗
╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝  ╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝░░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚══════╝
                                                                                 
'''                                                                              

#
def load_logo(path):
    # Function to load and return a PhotoImage
    try:
        return PhotoImage(file=path)
    except Exception as e:
        print(f"Error loading logo from {path}: {e}")
        return None
'''
def update_logo(event):
    # Rescale the logo based on the window size
    new_width = event.width // 10  
    new_height = event.height // 10  
    if new_width > 0 and new_height > 0:
        logo_img = load_logo('logoqut1.gif')  # Reload to prevent degradation
        logo_img = logo_img.zoom(new_width)  # Zoom in (make bigger)
        logo_img = logo_img.subsample(original_width)  # Then subsample (shrink down)
        logo.config(image=logo_img)
        logo.image = logo_img

'''


import html
# Main window setup

# Create the main window





def parse_rss_feed(xml_content,foo):
    item_pattern = r'<item>(.*?)</item>'
    title_pattern = r'<title>(.*?)</title>'
    link_pattern = r'<link>(.*?)</link>'
    date_pattern = r'<pubDate>(.*?)</pubDate>'
    items = findall(item_pattern, xml_content, DOTALL)
    
    if not items:
        print("No <item> elements found in the RSS feed.")
        return None

    # Extract and print only the first title and link

    #Both above and below are a lot of typing, could be reduced with OOP invoking self arguement for the corresponding relations
    first_item = items[0]
    title_match = search(title_pattern, first_item, DOTALL)
    link_match = search(link_pattern, first_item, DOTALL)
    date_match = search(date_pattern,first_item, DOTALL)
    if title_match and link_match and date_match:
        title = title_match[1]
        link = link_match[1]
        dateline = date_match[1]
        print(f"Title: {title}")
        print(f"Link: {link}\n")
        print(f"Dateline: {dateline}\n")
        #print(f"Full item content: {first_item}\n")
        #This could also be boolean but i've made it this in case i need to add more functions down the line
        if foo == 0:
            return link
        if foo == 1:
            return title
        if foo == 2:
            return dateline
        
    else:
        print(f"Failed to parse title or link from the first item: {first_item}")
        return None


'''Found better way [above].
def extract_text(html_content,p1):
    # Regex pattern to match the specific span text
    pattern = r'<span class="KeyboardFocus_keyboardFocus__NLJda" data-component="KeyboardFocus">(.*?)</span>'
    match = search(pattern, html_content)
    if match:
        return html.unescape(match.group(1))
    return None

'''

def show_latest_summary():
    # Function to simulate showing the latest summary of the selected news.
    selected_source = data_source_var.get()
    if selected_source == '':
        status_var.set('Please select a source first')
        
    if selected_source == 'Source A':
        status_var.set(f"Displaying the latest summary for' {selected_source}.")
            # Download the web page content
        # URL of the RSS feed
        rss_url = "http://www.9news.com.au/rss"

        # Downloading the content from the RSS feed
        xml_content = download(rss_url)
        if xml_content:
            parsed_item = parse_rss_feed(xml_content,1)
            status_var.set(parsed_item)
            if not parsed_item:
                print("No items found in the RSS feed.")
        else:
            print("Failed to download content.")
            # Specify the regex used to webscrape the info
    if selected_source == 'Source B':
        status_var.set(f"Displaying the latest summary for' {selected_source}.")
            # Download the web page content
        # URL of the RSS feed
        rss_url = "https://abcnews.go.com/abcnews/topstories"

        # Downloading the content from the RSS feed
        xml_content = download(rss_url)
        if xml_content:
            # this removes cdata, cdata which is quite valuable as it represents characters that are not used
            #for formatting the document however the regex command before already sorts this and i dont want to change it
            #as 2 of the 3 dont use cdata types for their xml outputs, therefore im just going to hacky workaround below
            #by replacing the characters with an empty string
            #a better way is to properly parse data types through using ET.fromstring twice to extract the data type
            #(or use beautifulsoup which is not allowed)

            parsed_item = parse_rss_feed(xml_content,1).replace("<![CDATA[", "").replace("]]>", "")

            status_var.set(parsed_item)
            if not parsed_item:
                print("No items found in the RSS feed.")
        else:
            print("Failed to download content.")
            
    if selected_source == 'Source C':
        status_var.set(f"Displaying the latest summary for' {selected_source}.")
            # Download the web page content
        # URL of the RSS feed
        rss_url = "https://www.brisbanetimes.com.au/rss/feed.xml"

        # Downloading the content from the RSS feed
        xml_content = download(rss_url)
        if xml_content:
            parsed_item = parse_rss_feed(xml_content,1)
            status_var.set(parsed_item)
            if not parsed_item:
                print("No items found in the RSS feed.")
        else:
            print("Failed to download content.")
            # Specify the regex used to webscrape the info
def show_full_details():
    
    selected_source = data_source_var.get()
    if selected_source == '':
        status_var.set('Please select a source first')
    else:
        status_var.set(f"Showing full details for {selected_source}.")
    if selected_source == 'Source A':
        status_var.set(f"Displaying the latest summary for' {selected_source}.")
            # Download the web page content
        # URL of the RSS feed
        rss_url = "https://www.brisbanetimes.com.au/rss/feed.xml"

        # Downloading the content from the RSS feed
        xml_content = download(rss_url)
        if xml_content:
            parsed_item = parse_rss_feed(xml_content,0)
            display_item = parse_rss_feed(xml_content,1)
            status_var.set(f'Showing latest details for{display_item}')
            urldisplay(parsed_item)
            if not parsed_item:
                print("No items found in the RSS feed.")
        else:
            print("Failed to download content.")
            # Specify the regex used to webscrape the info
    if selected_source == 'Source B':
        status_var.set(f"Displaying the latest summary for' {selected_source}.")
            # Download the web page content
        # URL of the RSS feed
        rss_url = "https://abcnews.go.com/abcnews/topstories"

        # Downloading the content from the RSS feed
        xml_content = download(rss_url)
        if xml_content:
            parsed_item = parse_rss_feed(xml_content,0).replace("<![CDATA[", "").replace("]]>", "")
            display_item = parse_rss_feed(xml_content,1)
            status_var.set(f'Showing latest details for{display_item}')
            urldisplay(parsed_item)
            if not parsed_item:
                print("No items found in the RSS feed.")
        else:
            print("Failed to download content.")
            # Specify the regex used to webscrape the info
    if selected_source == 'Source C':
        status_var.set(f"Displaying the latest summary for' {selected_source}.")
            # Download the web page content
        # URL of the RSS feed
        rss_url = "https://www.brisbanetimes.com.au/rss/feed.xml"

        # Downloading the content from the RSS feed
        xml_content = download(rss_url)
        if xml_content:
            parsed_item = parse_rss_feed(xml_content,0)
            display_item = parse_rss_feed(xml_content,1)
            status_var.set(f'Showing latest details for{display_item}')
            urldisplay(parsed_item)
            if not parsed_item:
                print("No items found in the RSS feed.")
        else:
            print("Failed to download content.")
            # Specify the regex used to webscrape the info

def save_rating():
    # Function to save the reliability rating.
    selected_source = data_source_var.get()
    rating = reliability_var.get()
    if selected_source == '':
        status_var.set('Please select a source first')
    else:
        # Fetch the latest news information for the selected source
        rss_url = None
        if selected_source == 'Source A':
            rss_url = "http://www.9news.com.au/rss"
        elif selected_source == 'Source B':
            rss_url = "https://abcnews.go.com/abcnews/topstories"
        elif selected_source == 'Source C':
            rss_url = "https://www.brisbanetimes.com.au/rss/feed.xml"
        
        if rss_url:
            xml_content = download(rss_url)
            if xml_content:
                headline = parse_rss_feed(xml_content, 1)
                dateline = parse_rss_feed(xml_content, 2)
                news_source = selected_source
                print(headline)
                print(dateline)
                print(news_source)
                print(str(rating))
                if headline and dateline:
                    status_var.set(f"Saving rating for {selected_source}.")
                    
                    # Initialize connection to database
                    connection = connect(database='reliability_ratings.db')
                    cursor = connection.cursor()
                    print(connection)
                    print(cursor)
                   
                    # Prepare the SQL query
                    sql = """
                    INSERT INTO ratings (news_source, headline, dateline, rating)
                    VALUES (?, ?, ?, ?)
                    
                    """
                    
                    # Execute the SQL query
                    cursor.execute(sql, (selected_source, headline, dateline, str(rating)))
                    
                    # Commit the changes and close the connection
                    connection.commit()
                    connection.close()
                    
                    status_var.set(f"Rating saved for {selected_source}.")
                else:
                    status_var.set("Failed to retrieve news information.")
            else:
                status_var.set("Failed to download content.")
        else:
            status_var.set("Invalid news source selected.")

def load_logo(path):
    # Function to load and return a PhotoImage
    try:
        #return PhotoImage(file=path)
        pass
    except Exception as e:
        print(f"Error loading logo from {path}: {e}")
        return None
def update_status(*args):
    selected_source = data_source_var.get()
    status_var.set(f"You have selected {selected_source}")




 

# Main window setup
mw = Tk()
mw.title("QUT Fact Checking Service")
mw.geometry('800x600')
mw.configure(background='lightblue')

# Load logo
original_logo_img = load_logo('logoqut1.gif')
if original_logo_img:
    logo = Label(mw, image=original_logo_img, bg='white')
    logo.grid(row=0, column=1, sticky='ne', padx=20, pady=20)

# Title logo
title_logo = Label(mw, text="QUT Fact Checker", bg="light blue", width=20, height=2, font=("Arial", 20))
title_logo.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

# Status bar to display messages
status_var = StringVar(mw, value="Welcome to QUT Fact Checking Service!")
status_label = Label(mw, textvariable=status_var, bg='white', fg='black', anchor='w')
status_label.grid(row=1, column=0, columnspan=2, sticky='ew', padx=10, pady=2)

# Data source selection
source_frame = LabelFrame(mw, text="Choose a Data Source:", bg='white')
source_frame.grid(row=2, column=0, padx=10, pady=10, sticky='w')
data_source_var = StringVar()
Radiobutton(source_frame, text="ABC", variable=data_source_var, value="Source A", bg='white').pack(anchor='w')
Radiobutton(source_frame, text="Sky News", variable=data_source_var, value="Source B", bg='white').pack(anchor='w')
Radiobutton(source_frame, text="QUT NEWS Hub", variable=data_source_var, value="Source C", bg='white').pack(anchor='w')

#
data_source_var.trace('w', update_status)


# Buttons for viewing news
button_frame = Frame(mw, bg='lightblue')
button_frame.grid(row=3, column=1, padx=10, pady=10, sticky='n')
Button(button_frame, text="Show Latest Summary", command=show_latest_summary, bg='light gray').pack(pady=5)
Button(button_frame, text="Show Full Details", command=show_full_details, bg='light gray').pack(pady=5)

# Data reliability selection and saving
reliability_frame = Frame(mw, bg='lightblue')
reliability_frame.grid(row=6, column=0, padx=10, pady=10, sticky='w')
Label(reliability_frame, text='Set Reliability Rating:', bg='white').pack(anchor='w')
reliability_var = IntVar(value=2)
Scale(reliability_frame, from_=0, to=5, variable=reliability_var, orient="horizontal", bg='white').pack(padx=20, pady=5, fill='x')
Button(reliability_frame, text="Save Rating", command=save_rating, bg='light gray').pack(pady=10)

# Show latest data and latest details
'''
show_latest_frame = Frame(mw, bg='lightblue')
show_latest_frame.grid(row=5,column=0,padx=20,pady=20,sticky='w')
#show_latest_frame
'''
# Configure grid
mw.grid_columnconfigure(0, weight=1)
mw.grid_columnconfigure(1, weight=1)

mw.mainloop()
