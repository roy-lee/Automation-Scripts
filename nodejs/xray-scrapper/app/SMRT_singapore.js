var Xray = require('x-ray');
var x = Xray({
  filters: {
    add: function (value) {
      return typeof value === 'string' ? "https://www.twitter.com" + value : value
    }
  }
});

var SingaporeTransportTweets = [
  "https://twitter.com/smrt_singapore",
  "https://twitter.com/ltatrafficnews",
  "https://twitter.com/sbstransit_ltd"
]

for (var i = 0; i < SingaporeTransportTweets.length; i++) {
  scrapeLink = SingaporeTransportTweets[i]

  try {
    x(scrapeLink, 'div.tweet', [{
      title: 'strong.fullname',
      tweet: '.tweet-text',
      link: '@data-permalink-path | add'
    }])(console.log)
        .write('results/SMRT_singapore.json');
  }
  /* TO-DO:
  1. Stop scrapping after 25th results
  2. Append JSON instead of overwriting file
  3. Exception handling
  */
  catch(err) {
    console.log("##### Reached end of page. #####");
  }

}
