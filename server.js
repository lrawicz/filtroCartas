var fs = require('fs');
var mkdirp = require('mkdirp');

fs.readFile('CSV/DB.csv', 'utf8', function(err, contents) {
    
	//Card number,Name,Rarity,Category,RAW,ID,booster
	//1          ,2   ,3     ,4       ,5  ,6 ,7

    var cards = contents.split("\n");
    cards.shift();
    for ( raw of cards) {
  		
  		card = raw.split(",")
  		var rarity = card[2]; //rarity
  		var ID = parseInt(card[5]); //ID
  		var booster = card[6]; //booster
  		console.log(booster);
  		var path = "output/BoostersOficiales/" + booster.trim() + "/" + rarity;
    	if (!fs.existsSync(path)) {
			mkdirp(path);  			
  		}
  	//	console.log ("asd");

  		


  		fs.copyFile('RAW/' + ID + '.png',  path + '/' + ID + '.png', (err) => {
		  if (err){
		  	console.log(err);
		  } else{
		  //	console.log('source.txt was copied to destination.txt');
		  }
		});
  		//process.exit(1);
	}
});
 
