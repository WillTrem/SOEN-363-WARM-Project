// List all users who do not post on instagram or do not tweet on twitter, and display the platform where the user doesn't post/tweet

use('project-phase-3-db');

db.userTwitter.aggregate([
  {
    $lookup: {
      from: "tweets",
      localField: "userId",
      foreignField: "userId",
      as: "tweets"
    }
  },
  {
    $lookup: {
      from: "instagramAccount",
      localField: "username",
      foreignField: "username",
      as: "userInstagram"
    }
  },
  {
    $match: {
      $or: [
        { tweets: { $size: 0 } },
        { "userInstagram.numberofposts": { $eq: 0 } }
      ]
    }
  },
  {
    $project: {
      _id: 0,
      username: 1,
      platform: {
        $cond: {
          if: { $gt: [{ $size: "$tweets" }, 0] },
          then: "Twitter",
          else: "Instagram"
        }
      }
    }
  }
]).toArray();
