// Lists the top 5 urls that are tweeted the most

use("project-phase-3-db");

db.links.aggregate([
    {
        $match: {
          url: { $ne: null }
        }
    },
    {
      $group: {
        _id: "$url",
        count: { $sum: 1 }
      }
    },
    {
      $sort: { count: -1 }
    },
    {
      $limit: 5
    },
    {
      $project: {
        _id: 0,
        url: "$_id",
        count: 1
      }
    }
  ])
  
