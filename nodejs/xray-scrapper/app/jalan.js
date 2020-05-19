var Xray = require('x-ray')
var x = Xray()

x('https://www.jalan.net/yad372546/kuchikomi/', '.kuchikomi-list-cassette', [
  {
      rating: ".score-number",
      title: ".text",
      commentTime: ".post-date"

  }
])
  .paginate('.next a@href')
  .limit(3)
  .write('results/jalan.json')