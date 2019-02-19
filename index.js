var fs = require('fs');
var mkdirp = require('mkdirp');

fs.readFile('DB.csv', 'utf8', function(err, contents) {
    
	//Card number,Name,Rarity,Category,RAW,ID,booster

    var cards = contents.split("\n");
    cards.shift();
    for ( raw of cards) {
  		
  		card = raw.split(",")
  		var rarity = card[2]; //rarity
  		var ID = card[5]; //ID
  		var booster = card[6]; //ID
  		console.log(booster);
  		var path = booster.trim() + "/" + rarity;
    	if (fs.existsSync(path)) {

  		}else{
  			mkdirp(path);
  		}
  		console.log ("asd");

  		


  		fs.copyFile('/RAW/' + ID + '.png', '/' + path + '/' + ID + '.png', (err) => {
		  if (err){
		  	console.log(err);
		  } else{
		  	console.log('source.txt was copied to destination.txt');
		  }
		});
  		//process.exit(1);
	}


fs.copyFile('source.txt', 'destination.txt', (err) => {
  if (err) throw err;
  console.log('source.txt was copied to destination.txt');
});

});
 
