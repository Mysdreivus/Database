DROP database IF EXISTS league;
CREATE database league;
USE league;

CREATE TABLE item(
    itemName VARCHAR(30) NOT NULL UNIQUE,
    descriptionItem TEXT NOT NULL,
    costOfItem INT NOT NULL,
    typeOfItem TEXT NOT NULL,
    PRIMARY KEY (itemName)
);

CREATE TABLE gameplay(
    gameplayType VARCHAR(15) NOT NULL UNIQUE,
    descriptionPlayStyle TEXT NOT NULL,
    teamBased TEXT NOT NULL,
    champOptimalSynergy VARCHAR(15) NOT NULL,
    PRIMARY KEY (gameplayType)
);

CREATE TABLE champion(
    championName VARCHAR(15) NOT NULL UNIQUE,
    numOfWinsChamp INT NOT NULL,
    numOfLossChamp INT NOT NULL,
    winLossRatioChamp DOUBLE NOT NULL,
    timePlayedCumulative INT NOT NULL,
    mostFrequentRole TEXT NOT NULL,
    learningDifficulty TEXT NOT NULL,
    itemsFrequentlyUsed1 VARCHAR(30) NOT NULL,
    itemsFrequentlyUsed2 VARCHAR(30) NOT NULL,
    itemsFrequentlyUsed3 VARCHAR(30) NOT NULL,
    gameplayType VARCHAR(15) NOT NULL,
    PRIMARY KEY (championName),
    FOREIGN KEY (itemsFrequentlyUsed1) REFERENCES item(itemName),
    FOREIGN KEY (itemsFrequentlyUsed2) REFERENCES item(itemName),
    FOREIGN KEY (itemsFrequentlyUsed3) REFERENCES item(itemName),
    FOREIGN KEY (gameplayType)         REFERENCES gameplay(gameplayType)
);

CREATE TABLE player(
    playerName VARCHAR(15) NOT NULL UNIQUE,
    mostPlayedChamp TEXT NOT NULL,
    champMostWins TEXT NOT NULL,
    timePlayed INT NOT NULL,
    numOfWinsPlayer INT NOT NULL,
    numOfLossesPlayer INT NOT NULL,
    winLossRatioPlayer DOUBLE NOT NULL,
    topChamp1 VARCHAR(15) NOT NULL,
    topChamp2 VARCHAR(15) NOT NULL,
    topChamp3 VARCHAR(15) NOT NULL,   
    PRIMARY KEY (playerName),
    FOREIGN KEY (topChamp1) REFERENCES champion(championName),
    FOREIGN KEY (topChamp2) REFERENCES champion(championName),
    FOREIGN KEY (topChamp3) REFERENCES champion(championName)
);

insert into item (itemName,descriptionItem,costOfItem,typeOfItem)
            VALUES ("Aegis","For Protection",2400,"SupportItem");
insert into item (itemName,descriptionItem,costOfItem,typeOfItem)
            VALUES ("Locket","For Shielding",2500,"SupportItem");
insert into item (itemName,descriptionItem,costOfItem,typeOfItem)
            VALUES ("Ward","For Vision",2350,"SupportItem");
insert into item (itemName,descriptionItem,costOfItem,typeOfItem)
            VALUES ("Phantom Dancer","For Attack Speed and Critical Chance",2450,"MarksmanItem");
insert into item (itemName,descriptionItem,costOfItem,typeOfItem)
            VALUES ("Blade of the Ruined King","For Attack Speed and Percent Damage",3100,"MarksmanItem");
insert into item (itemName,descriptionItem,costOfItem,typeOfItem)
            VALUES ("Infinity Edge","For Critical Chance and Critical Damage",3400,"MarksmanItem");
insert into item (itemName,descriptionItem,costOfItem,typeOfItem)
            VALUES ("Righteous Glory","For Movement Speed",2150,"TankItem");
insert into item (itemName,descriptionItem,costOfItem,typeOfItem)
            VALUES ("Steraks","For Health",3600,"TankItem");
insert into item (itemName,descriptionItem,costOfItem,typeOfItem)
            VALUES ("Thornmail","For Armor",3400,"TankItem");
insert into item (itemName,descriptionItem,costOfItem,typeOfItem)
            VALUES ("Guinsoos","For Pure Mix Damage",3800,"DeulistItem");
insert into item (itemName,descriptionItem,costOfItem,typeOfItem)
            VALUES ("Luden's Echo","For Magic Damage",3800,"MageItem");
insert into item (itemName,descriptionItem,costOfItem,typeOfItem)
            VALUES ("Void Staff","For Magic Defence Penetration",3400,"MageItem");
insert into item (itemName,descriptionItem,costOfItem,typeOfItem)
            VALUES ("Zhonya's","For Mage's Defence",3100,"MageItem");

insert into gameplay (gameplayType,descriptionPlayStyle,teamBased,champOptimalSynergy)
            VALUES ("Support","Protect the Marksman",'Yes',"Vayne");
insert into gameplay (gameplayType,descriptionPlayStyle,teamBased,champOptimalSynergy)
            VALUES ("Marksman","Stick to the Support",'Yes',"Alistar");
insert into gameplay (gameplayType,descriptionPlayStyle,teamBased,champOptimalSynergy)
            VALUES ("Tank","Block for your team",'No',"Alistar");
insert into gameplay (gameplayType,descriptionPlayStyle,teamBased,champOptimalSynergy)
            VALUES ("Duelist","Specializes in duels",'No',"Cho'gath");
insert into gameplay (gameplayType,descriptionPlayStyle,teamBased,champOptimalSynergy)
            VALUES ("Mage","Burst other players",'No',"Alistar");


insert into champion (championName,numOfWinsChamp,numOfLossChamp,winLossRatioChamp,timePlayedCumulative,mostFrequentRole,learningDifficulty,itemsFrequentlyUsed1,itemsFrequentlyUsed2,itemsFrequentlyUsed3,gameplayType)
            VALUES ("Alistar",300,250,54.54,400,"Bottomlane","Expert","Ward","Aegis","Locket","Support");
insert into champion (championName,numOfWinsChamp,numOfLossChamp,winLossRatioChamp,timePlayedCumulative,mostFrequentRole,learningDifficulty,itemsFrequentlyUsed1,itemsFrequentlyUsed2,itemsFrequentlyUsed3,gameplayType)
            VALUES ("Cho'gath",295,300,49.58,465,"Toplane","Beginner","Righteous Glory","Steraks","Thornmail","Tank");
insert into champion (championName,numOfWinsChamp,numOfLossChamp,winLossRatioChamp,timePlayedCumulative,mostFrequentRole,learningDifficulty,itemsFrequentlyUsed1,itemsFrequentlyUsed2,itemsFrequentlyUsed3,gameplayType)
            VALUES ("Master Yi",325,275,54.16,425,"Jungle","Intermediate","Guinsoos","Steraks","Infinity Edge","Duelist");
insert into champion (championName,numOfWinsChamp,numOfLossChamp,winLossRatioChamp,timePlayedCumulative,mostFrequentRole,learningDifficulty,itemsFrequentlyUsed1,itemsFrequentlyUsed2,itemsFrequentlyUsed3,gameplayType)
            VALUES ("Ahri",300,250,54.54,400,"Midlane","Beginner","Luden's Echo","Void Staff","Zhonya's","Mage");
insert into champion (championName,numOfWinsChamp,numOfLossChamp,winLossRatioChamp,timePlayedCumulative,mostFrequentRole,learningDifficulty,itemsFrequentlyUsed1,itemsFrequentlyUsed2,itemsFrequentlyUsed3,gameplayType)
            VALUES ("Vayne",345,220,61.06,445,"Bottomlane","Expert","Phantom Dancer","Blade of the Ruined King","Infinity Edge","Marksman");

insert into player (playerName,mostPlayedChamp,champMostWins,timePlayed,numOfWinsPlayer,numOfLossesPlayer,winLossRatioPlayer,topChamp1,topChamp2,topChamp3)
            VALUES ("theBeast","Cho'gath",234,155,254,170,59.91,"Cho'gath","Vayne","Alistar");
insert into player (playerName,mostPlayedChamp,champMostWins,timePlayed,numOfWinsPlayer,numOfLossesPlayer,winLossRatioPlayer,topChamp1,topChamp2,topChamp3)
            VALUES ("hide the bush","Ahri",150,132,223,155,58.99,"Ahri","Alistar","Master Yi");
insert into player (playerName,mostPlayedChamp,champMostWins,timePlayed,numOfWinsPlayer,numOfLossesPlayer,winLossRatioPlayer,topChamp1,topChamp2,topChamp3)
            VALUES ("naruDo","Alistar",188,145,210,180,53.85,"Alistar","Vayne","Ahri");
insert into player (playerName,mostPlayedChamp,champMostWins,timePlayed,numOfWinsPlayer,numOfLossesPlayer,winLossRatioPlayer,topChamp1,topChamp2,topChamp3)
            VALUES ("asotelo","Master Yi",229,160,245,165,59.76,"Master Yi","Vayne","Cho'Gath");
insert into player (playerName,mostPlayedChamp,champMostWins,timePlayed,numOfWinsPlayer,numOfLossesPlayer,winLossRatioPlayer,topChamp1,topChamp2,topChamp3)
            VALUES ("fakest","Vayne",192,143,196,115,63.02,"Vayne","Ahri","Master Yi");
