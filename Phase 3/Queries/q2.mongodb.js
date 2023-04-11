// Lists number of tweets & the average and maximum follower count for users who have Twitter and Instagram

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
           _id: null ,
           tweet_count: { $sum: 1 },
           avg_twitter_follower_count: { $avg: "$followercount" },
           max_insta_follower_count: { $max: "$instagramAccount.followercount" }
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
           tweet_count: 1,
           avg_twitter_follower_count: 1,
           max_insta_follower_count: 1
         }
   }
]).toArray();
