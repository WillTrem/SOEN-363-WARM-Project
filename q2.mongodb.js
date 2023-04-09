// Another query can be the following as it provides information about the number of tweets and the average and maximum follower count for each user who has a Twitter and Instagram account.

use('project-phase-3-db');

db.userTwitter.aggregate([
   {
      $lookup:
         {
           from: "tweets",
           localField: "userId",
           foreignField: "userId",
           as: "tweets"
         }
   },
   {
      $unwind: "$tweets"
   },
   {
      $lookup:
         {
           from: "instagramaccount",
           localField: "username",
           foreignField: "username",
           as: "instagramAccount"
         }
   },
   {
      $unwind: "$instagramAccount"
   },
   {
      $group:
         {
           _id: "$username",
           tweet_count: { $sum: 1 },
           avg_twitter_follower_count: { $avg: "$followercount" },
           max_insta_follower_count: { $max: "$instagramaccount.followercount" }
         }
   },
   {
      $sort:
         {
           tweet_count: -1
         }
   },
   {
      $project:
         {
           _id: 0,
           username: "$_id",
           tweet_count: 1,
           avg_twitter_follower_count: 1,
           max_insta_follower_count: 1
         }
   }
]).toArray();
