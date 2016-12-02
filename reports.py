def count_games(file_name):
    gamedata=[]
    gamelist=open(file_name,"r")
    numberofgames=0
    for line in gamelist:
        gamedata.append(line.strip().split("\t"))
    for i in range(0,len(gamedata),1):
        numberofgames+=1
    return numberofgames

def decide(file_name,year):
        gamedata=[]
        gamelist=open(file_name,"r")
        yearindex=2
        booleanvar=0
        for line in gamelist:
            gamedata.append(line.strip().split("\t"))
        for i in range(0,len(gamedata),1):
            if int(gamedata[i][yearindex])==int(year):
                booleanvar=1
        print(booleanvar)
        return booleanvar

def get_latest(file_name):
        gamelist=open(file_name,"r")
        gamedata=[]
        latest=0
        latestgametitle=""
        titleindex=0
        yearindex=int(2)
        for line in gamelist:
            gamedata.append(line.strip().split("\t"))
        for i in range(0,len(gamedata),1):
            if int(latest)<int(gamedata[i][yearindex]):
                latest=gamedata[i][yearindex]
                latestgametitle=gamedata[i][titleindex]
        print(latestgametitle)
        return latestgametitle

def count_by_genre(file_name,genre):
    gamedata=[]
    gamelist=open(file_name,"r")
    genreindex=3
    givengenre=0
    for line in gamelist:
        gamedata.append(line.strip().split("\t"))
    for i in range(0,len(gamedata),1):
        if gamedata[i][genreindex]==genre:
            givengenre+=1
    print(givengenre)
    return givengenre

def get_line_number_by_title(file_name,title):
        gamedata=[]
        gamelist=open(file_name,"r")
        titleline=0
        for line in gamelist:
            gamedata.append(line.strip().split("\t"))
        for i in range(0,len(gamedata),1):
                if gamedata[i][0]==title:
                    titleindex=i+1
        print(titleindex)
        return titleindex

def sort_abc(file_name):
    gamedata=[]
    gamelist=open(file_name,"r")
    sortedgamedata=[]
    titleindex=0
    for line in gamelist:
        gamedata.append(line.strip().split("\t"))
    temporary=gamedata[0][0]
    for i in range(0,len(gamedata),1):
        if gamedata[i][0]<=str(temporary):
            temporary=gamedata[i][0]
            sortedgamedata.append(temporary)
            print(temporary)
    return sortedgamedata

def get_genres(file_name):
    gamedata=[]
    gamelist=open(file_name,"r")
    genreindex=3
    genres=[]
    for line in gamelist:
        gamedata.append(line.strip().split("\t"))
    for i in range(0,len(gamedata),1):
        if gamedata[i][genreindex] not in genres:
            genres.append(gamedata[i][genreindex])
    list.sort(genres)
    return genres

def when_was_top_sold_fps(file_name):
        gamelist=open(file_name,"r")
        gamedata=[]
        yearindex=2
        soldindex=1
        soldyear=0
        genreindex=3
        topsoldcopies=0
        for line in gamelist:
            gamedata.append(line.strip().split("\t"))
        for i in range(0,len(gamedata),1):
            if topsoldcopies<float(gamedata[i][soldindex]) and gamedata[i][genreindex]=='First-person shooter':
                topsoldcopies=float(gamedata[i][soldindex])
                soldyear=float(gamedata[i][yearindex])
        print((topsoldcopies,soldyear))
        return soldyear
