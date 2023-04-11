// This query returns a list of all the UserTwitter usernames that have matching usernames in the InstagramAccount table, with duplicates that are removed. These two tables combined into one single query help to identify patterns and relationships that might not be apparent from looking at each database separately by its own.

use('project-phase-3-db');

db.userTwitter.aggregate([
  { 
    $lookup: 
    {
        from: "instagramaccount",
        localField: "username",
        foreignField: "username",
        as: "instagramaccount"
    }
  },
  {
    $match: 
    {
      "instagramaccount": {$ne:[]}
    }
  },
  {
    $group: 
    {
      _id: "$username",
    }
  },
]).toArray();
