// Lists the username that has the most follower count in instagram


use('project-phase-3-db');
db.instagramaccount.aggregate([
   { $sort: { followercount: -1 } }, 
   { $limit: 1 }, 
   { $project: { _id: 0, username: 1, followercount:1  } } 
 ]).toArray();
 