//  Displays the time of the day that has the greatest number of tweets being tweeted

use("project-phase-3-db");

db.tweet.aggregate([
  {
    $group: {
        _id: { $substr: ["$datetime", 11, 12] },


      count: { $sum: 1 }
    }
  },
  { $sort: { count: -1 } },
  { $limit: 1 },
  { $project: { hourOfDay: "$_id", _id: 0, count:1 } }
])
