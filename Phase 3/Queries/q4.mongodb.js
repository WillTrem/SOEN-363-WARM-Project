// Lists Twitter users’ average number of followers from 2020 to 2023

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
  