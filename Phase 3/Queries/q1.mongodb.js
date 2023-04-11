// Lists usernames who have same usernames in Twitter and Instagram (duplicates removed)

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
