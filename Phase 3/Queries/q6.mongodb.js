// Lists the top 5 tweets that are the most liked and contain the word “Instagram”

use("project-phase-3-db");

db.tweet.aggregate([
    {
      $lookup: {
        from: "tweetmetrics",
        localField: "_id",
        foreignField: "tweetid",
        as: "metrics"
      }
    },
    {
      $match: {
        text: { $regex: /Instagram/i }
      }
    },
    {
      $unwind: "$metrics"
    },
    {
      $sort: { "metrics.favoritecount": -1 }
    },
    {
      $limit: 5
    },
    {
      $project: {
        _id: 0,
        tweetid: 1,
        text: 1,
        favoritecount: "$metrics.favoritecount"
      }
    }
]).toArray();
  