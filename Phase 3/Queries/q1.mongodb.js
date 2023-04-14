// Lists usernames who have same usernames in Twitter and Instagram (duplicates removed) with number of usernames

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
  {
    $group:
    {
      _id: null,
      usernames: { $addToSet: "$_id" }
    }
  },
  {
    $project:
    {
      _id: 0,
      usernames: 1,
      count: { $size: "$usernames" }
    }
  }
]).toArray();

