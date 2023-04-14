// Lists the usernames who have the most followers in twitter or instagram

use("project-phase-3-db");

db.userTwitter.aggregate([
    {
      $lookup: {
        from: "instagramAccount",
        localField: "username",
        foreignField: "username",
        as: "instagramAccounts"
      }
    },
    {
      $addFields: {
        followerscountTwitter: "$followercount",
        followerscountInstagram: { $sum: "$instagramAccounts.followercount" },
        platform: {
          $cond: {
            if: { $gt: ["$followercount", { $sum: "$instagramAccounts.followercount" }] },
            then: "Twitter",
            else: "Instagram"
          }
        }
      }
    },
    {
      $project: {
        _id: 0,
        username: 1,
        followerscount: {
          $max: ["$followerscountTwitter", "$followerscountInstagram"]
        },
        platform: 1
      }
    },
    {
      $sort: { followerscount: -1 }
    },
    {
      $limit: 5
    }
  ]);
  