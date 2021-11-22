import shutil
#template\Header.txt
#template\Menu.txt
#template\Body.txt
#template\Footer.txt

def MergeTemplate(PassedFileName):
    with open('../'+ PassedFileName +'.html','wb') as wfd:
        for f in ['../template/Header.txt','../template/Menu.txt','temp.txt','../template/Body.txt','../template/Footer.txt']:
            with open(f,'rb') as fd:
                shutil.copyfileobj(fd, wfd)


def ReadFile():
    #Clear File
    f = open("temp.txt", "w")
    f.write('<h1>Games</h1>\n')
    f.write('<p>Currently there are no downloads at this moment as I am currently creating a menu system so you only have to download a pack of games.</p>\n')
    f.close()

    #Create File
    db = open("games.txt", "r")

    #Name of Game^Programmed in^year^image path^text^ download link^ video link^

    for xdb in db:
        #xdb = db.readline()
        g = ""
        #print(xdb)
        if len(xdb)>5:
            first_chars = xdb[0:3]
            if first_chars != "###":      
                g = xdb.split("^")
                print(g[0])
                f = open("temp.txt", "a")
                f.write('<table><tr><td><img src="'+ str(g[3]) +'" class="w3-hover-opacity w3-border" alt="Image">\n')
                f.write('</td><td class="w3-padding-large">\n')
                f.write('<h3>' + g[0] + ' (' + g[1] + ')</h3>\n')
                f.write('<i class="w3-tag">Coded using: ' + g[2] + '</i><br>\n')
                f.write('<i>' + g[4] + '</i>\n')
                f.write('</td></tr></table>\n\n')
                f.close()
    db.close()
    MergeTemplate("Games")

    

def ReadFileComputers():
    #Clear File
    f = open("temp.txt", "w")
    f.write('<h1>Computers</h1>\n')
    f.write('<p>My brief history of first computers that I can remember, Many PCs are not here after the year 2000 as they swapped and changed so often. The PCs listed are the ones that hold the most memorys.</p>\n')
    f.close()

    #Create File
    db = open("computers.txt", "r")


##### Name of computer   ^   TEXT 				^ IMAGE 	^ YEAR 			^ Owned ^
##### 0                      1                   2          3                4         

    for xdb in db:
        #xdb = db.readline()
        g = ""
        #print(xdb)
        if len(xdb)>5:
            first_chars = xdb[0:3]
            if first_chars != "###":      
                g = xdb.split("^")
                print(g[0])
                f = open("temp.txt", "a")
                f.write('<table><tr><td><img src="'+ str(g[2]) +'" class="w3-circle w3-grayscale-max w3-hover-opacity w3-border" alt="Image">\n')
                f.write('</td><td class="w3-padding-large">\n')
                f.write('<h3>' + g[0] + ' (' + g[3] + ')</h3>\n')
                
                checkown = g[4]
                if checkown == "Yes":
                    f.write('<p class="w3-tag">Currently Own</p><br>\n')
                
                f.write('<i>' + g[1] + '</i>\n')
                f.write('</td></tr></table>\n\n')
                f.close()
    db.close()
    MergeTemplate("Computers")


    

    
    
    ##### Name of Album   ^ IMAGE 	^ Tracks ^ Youtube Link ^
##### 0                 1            2          3            
    
def ReadFileMusic():
    #Clear File
    f = open("temp.txt", "w")
    f.write('<h1>Music</h1>\n')
    f.write('<p>Some of the music created can be found here and on youtube. Most was created using pre-made loops etc, however all new music from 2017 onwards (Currently still working on) will be made from scratch and no pre-made loops/pattens.</p>\n')
    f.write('<p>All tracks are free to use for anything including youtube and games. All I ask is to just give me credit and would be nice to know what they are used for.</p>\n')
    f.close()

    #Create File
    db = open("music.txt", "r")

    for xdb in db:
        #xdb = db.readline()
        g = ""
        #print(xdb)
        if len(xdb)>5:
            first_chars = xdb[0:3]
            if first_chars != "###":      
                g = xdb.split("^")
                print(g[0])
                f = open("temp.txt", "a")
                f.write('<table><tr><td><img src="'+ str(g[1]) +'" class="w3-hover-opacity w3-border" alt="Image">\n')
                f.write('</td><td class="w3-padding-large">\n')
                f.write('<h3>' + g[0] + '</h3>\n')
                
                
                f.write('<i>' + g[2] + '</i>\n')
              #youtube link needed
                f.write('<br><div class="w3-tag w3-red"><a href="' + g[3] + '">YouTube Link</a></div>\n')


                f.write('</td></tr></table>\n\n')
                f.close()
    db.close()
    MergeTemplate("Music")
    
    
    
def ReadFileApps():
    #Clear File
    f = open("temp.txt", "w")
    f.write('<h1>Applications</h1>\n')
    f.write('<p>Over the years there has also been many websites / web systems that I created but as time have moved on these now look very dated and at the moment are not shown on this page. They will be added later at some point as a history reference.I am currently working on downloads for everything possible, these will be available later.</p>\n')
    f.close()

    #Create File
    db = open("apps.txt", "r")
##### Name of Program  ^ Coded in ^ IMAGE 	^ Info ^ Owned ^ Link ^
##### 0                 1            2          3      4     5 
    for xdb in db:
        #xdb = db.readline()
        g = ""
        #print(xdb)
        if len(xdb)>5:
            first_chars = xdb[0:3]
            if first_chars != "###":      
                g = xdb.split("^")
                print(g[0])
                f = open("temp.txt", "a")
                f.write('<table><tr><td><img src="'+ str(g[2]) +'" class="w3-hover-opacity w3-border" alt="Image">\n')
                f.write('</td><td class="w3-padding-large">\n')
                f.write('<h3>' + g[0] + '</h3>\n')
                
                
                f.write('<i>' + g[3] + '</i>\n')
              #youtube link needed
                #f.write('<br><div class="w3-tag w3-red"><a href="' + g[3] + '">YouTube Link</a></div>\n')
                checkown = g[4]
                if checkown == "Yes":
                    f.write('<p class="w3-tag">Owned By Company (Code not available)</p><br>\n')
                

                f.write('</td></tr></table>\n\n')
                f.close()
    db.close()
    MergeTemplate("Applications")
    


def ReadFileProjects():
    #Clear File
    f = open("temp.txt", "w")
    f.write('<h1>Projects</h1>\n')
    f.write('<p>These are all mini projects that have been created. The goal is to make sure the cost is under 20 Pounds and for it to be intresting and to learn something from it.</p>\n')
    f.close()

    #Create File
    db = open("projects.txt", "r")
##### Name of Project  ^ Year ^ IMAGE1 	^ IMAGE2 ^ Info ^ Link ^
##### 0                 1           2       3      4     5                1            2          3      4     5 
    for xdb in db:
        #xdb = db.readline()
        g = ""
        #print(xdb)
        if len(xdb)>5:
            first_chars = xdb[0:3]
            if first_chars != "###":      
                g = xdb.split("^")
                print(g[0])
                f = open("temp.txt", "a")
                
                #f.write('<div class="w3-panel w3-dark-grey"><p>' + g[0] + ' ('+ g[1] +')</p></div>\n')
                f.write('<p class="w3-tag">' + g[0] + ' ('+ g[1] +')</p><br>\n')
               
                f.write('<table><tr><td><center><img src="'+ str(g[2]) +'" class="w3-hover-opacity w3-border" alt="Image"></center></td>\n')
                f.write('<td><center><img src="'+ str(g[3]) +'" class="w3-hover-opacity w3-border" alt="Image"></center></td></tr>\n')
                f.write('<tr><center><td class="w3-padding-large" colspan="2"></center>\n')
                
                
                
                f.write('<i><center>' + g[4] + '</center></i>\n')

                f.write('</td></tr></table>\n\n')
                f.close()
    db.close()    
    MergeTemplate("Projects")

def MergeTemplateHome(PassedFileName):
    with open('../'+ PassedFileName +'.html','wb') as wfd:
        for f in ['../template/Header.txt','../template/Menu.txt','../template/Home_Page.txt','../template/Body.txt','../template/Footer.txt']:
            with open(f,'rb') as fd:
                shutil.copyfileobj(fd, wfd)


#RUN#
ReadFile() #Games
#ReadFileProjects()
#ReadFileApps()
#ReadFileMusic()
#ReadFileComputers()

MergeTemplateHome("index")  


