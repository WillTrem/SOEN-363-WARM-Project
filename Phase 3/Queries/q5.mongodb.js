// Displays the month that has the greatest number of twitter user created between 2022-23

use('project-phase-3-db');

db.userTwitter.aggregate([ 
    {
        $match: {
          created: {
            $gte: "2022-01-01",
            $lte: "2023-01-01"
          }
        }
    },
    {
      $group: {
        _id: { $substr: ["$created", 0, 7] },
        count: { $sum: 1 } 
      }
    },
    {
      $sort: { count: -1 }
     },
     {
      $limit: 1
    }
]);