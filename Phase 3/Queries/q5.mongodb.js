// Lists the number of Twitter user created each month in the past year between 2022 and 2023.

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
        $sort:
           {
             _id: 1
           }
     },
]);