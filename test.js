var watermark = require('dynamic-watermark');
//var watermarkViejo = require('imagemagick-dynamic-watermark');

var optionsImageWatermark = {
    type: "image",
    source: "27551.png",
    logo: "fondo_negro.png", // This is optional if you have provided text Watermark
    destination: "output.png",
    position: {
        logoX : 260,
        logoY : 250,
        logoHeight: 100,
        logoWidth: 100
    }
};

//optionsImageWatermark or optionsTextWatermark
watermark.embed(optionsImageWatermark, function(status) {
    //Do what you want to do here
	var optionsTextWatermark = {
	    type: "text",
	    text: "QWE", // This is optional if you have provided text Watermark
	    destination: "output2.png",
	    source: "output.png",
	    position: {
	        logoX : 260,
	        logoY : 420,
	        logoHeight: 200,
	        logoWidth: 200
	    },
	    textOption: {
	        fontSize: 20, //In px default : 20
	        color: '#AAF122' // Text color in hex default: #000000

	    }
	};

	//optionsImageWatermark or optionsTextWatermark
	watermark.embed(optionsTextWatermark, function(status) {
	    //Do what you want to do here
	    console.log(status);
	});
});







var optionsTextWatermark = {
    type: "text",
    text: "QWE", // This is optional if you have provided text Watermark
    destination: "output.png",
    source: "27551.png",
    position: {
        logoX : 260,
        logoY : 420,
        logoHeight: 200,
        logoWidth: 200
    },
    textOption: {
        fontSize: 20, //In px default : 20
        color: '#AAF122' // Text color in hex default: #000000

    }
};

//optionsImageWatermark or optionsTextWatermark
watermark.embed(optionsTextWatermark, function(status) {
    //Do what you want to do here
    console.log(status);
});