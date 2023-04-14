// Display the user who has the highest number of instagram_posts or tweets  (for users having a Twitter and Instagram account) 

use("project-phase-3-db");

db.instagramaccount.aggregate([
    {
      $lookup: {
        from: "userTwitter",
        localField: "username",
        foreignField: "username",
        as: "twitter"
      }
    },
    {
      $addFields: {
        tweet_count: { $size: "$twitter" },
      },
    },
    {
      $project: {
        _id: 0,
        username: 1,
        instagram_count: "$numberofposts",
        tweet_count: 1,
        highest_count: { $max: ["$numberofposts", "$tweet_count"] }
      }
    },
    {
      $sort: { highest_count: -1 }
    },
    {
      $limit: 1
    }
  ]).toArray();
  