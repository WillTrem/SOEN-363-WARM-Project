// This query the average number of followers for Twitter users between 2020 and 2023.

use('project-phase-3-db');

db.userTwitter.aggregate([
    {
      $match: {
        created: {
          $gte: "2020-01-01",
          $lte: "2023-01-01"
        }
      }
    },
    {
      $group: {
        _id: null,
        avg_followers: {
          $avg: "$followercount"
        }
      }
    },
    {
        $project: {
            _id: 0,
            avg_followers: 1,   
            }
    }
  ])
  