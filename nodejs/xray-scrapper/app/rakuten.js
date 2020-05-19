var Xray = require('x-ray')
var x = Xray()

x('https://review.travel.rakuten.co.jp/hotel/voice/4853', '.commentBox', [
  {
      rating: ".commentRate",
      title: ".commentTitle",
      comment: ".commentSentence",
      purpose: ".commentPurpose",
      commentTime: ".time"

  }
])(console.log)
  .paginate('.pagingNext a@href')
//   .limit(3)
  .write('results/rakuten.json')